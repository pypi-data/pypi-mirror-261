import asyncio
import mimetypes
import os
import requests
import time

from pydantic import model_validator, Field
from requests import HTTPError
from requests_toolbelt import MultipartEncoder
from typing import Literal, Optional

from mediqbox.abc.abc_component import *
from mediqbox.download import *
from mediqbox.act.helpers import *

class ActConfig(ComponentConfig):
  username: str
  password: str
  token: Optional[str] = None
  team_id: Optional[str] = None
  working_dir: Optional[str] = None
  max_retries: int = Field(ge=1, le=3, default=3)
  timeout: int = Field(ge=1, default=600) # in seconds

class ActInputData(InputData):
  texts: list[str] = []
  files: list[str] = []
  source_lang: Literal['zh', 'en'] = 'en'
  target_lang: Literal['zh', 'en'] = 'zh'
  tm_ids: Optional[list[int]] = None
  tb_ids: Optional[list[int]] = None

  @model_validator(mode='after')
  def check_input_texts_or_files(self) -> 'ActInputData':
    if len(self.texts) == 0 and len(self.files) == 0:
      raise ValueError("`texts` and `files` are both empty")
    
    return self
  
  @model_validator(mode='after')
  def check_language_directions(self) -> 'ActInputData':
    if self.source_lang == self.target_lang:
      raise ValueError("`source_lang` and `target_lang` are same")
    
    return self

class ActTooManyRetriesException(Exception):
  """Exception raised when too many retries occur in accessing ACT"""
  def __init__(self, retries: int, message: str="Too many retries", *args):
    super().__init__(f"{message}: {retries} attempts made", *args)

class ActConfigException(Exception):
  """Exception raised for missing or invalid field(s) in config"""
  def __init__(self, name: str, message: str="Invalid ActConfig", * args):
    super().__init__(f"{message}: field name {name}", *args)

class ActError(Exception): ...

class Act(AbstractComponent):
  base_url: str = "https://fanyi.atman360.com"
  api_base_url: str = "https://fanyi.atman360.com/api"
  max_batch_size: int = 5000

  @property
  def post_headers(self) -> dict[str, str]:
    return {
      "Content-Type": "application/json",
      "Authorization": f"Token {self.config.token}"
    } if self.config.token else {
      "Content-Type": "application/json"
    }

  def login(self) -> None:
    """ Login to an ACT account """
    if self.config.token:
      return
    
    url = f"{self.api_base_url}/user/login/"
    res = requests.post(
      url, headers=self.post_headers,
      json={'username': self.config.username, 'password': self.config.password}
    )

    if res.ok:
      res = res.json()
      if is_act_result_ok(res):
        self.config.token = res['data']['authtoken']
      else:
        raise ValueError(f"Failed to login to ACT: {res['msg']}")
    else:
      raise HTTPError(url, res.status_code, res.reason)

    # Get team_id if possible
    url = f"{self.api_base_url}/user/profile/"
    res = requests.get(
      url, headers=self.post_headers
    ).json()

    if is_act_result_ok(res):
      if res['data'].get('member'):
        self.config.team_id = str(res['data']['member'][0]['team_id'])
    else:
      raise ValueError(f"Failed to access user profile: {res['msg']}")
    
    return
  
  def translate_batch(
      self,
      batch: list[str],
      input_data: ActInputData
  ) -> list[str]:
    """
    Translate a batch of texts

    :param batch: List of texts to be translated
    :param input_data: The input data from `process` method
    :return: List of translated texts
    """
    data = {k:v for k,v in {
      'domain': 'medical',
      'lines': texts_to_act_lines(batch),
      'source': input_data.source_lang,
      'target': input_data.target_lang,
      'tm_ids': input_data.tm_ids,
      'tb_ids': input_data.tb_ids
    }.items() if v is not None}

    url = f"{self.api_base_url}/trans/batch/?team_id={self.config.team_id}"
    retries = self.config.max_retries

    while retries:
      response = requests.post(url, headers=self.post_headers, json=data)

      if response.ok:
        result = response.json()
        if is_act_result_ok(result):
          return act_lines_to_texts(result['data'])
        
        log_act_result_error(result)
      else:
        log_act_response_error(response)
      
      retries -= 1
    
    raise ActTooManyRetriesException(
      self.config.max_retries,
      "Failed to access ACT's translate_batch service after multiple retries"
    )

  def translate_long_line(
      self,
      long_line: str,
      input_data: ActInputData
  ) -> str:
    """
    Translate a long line that exceeds `max_batch_size` characters

    :param long_line: The long line text
    :param input_data: The input data from `process` method
    :return: The translated text
    """
    sentences = split_sentences(long_line, lang=input_data.source_lang)
    texts = []
    translated = []

    while len(sentences):
      sent = sentences.pop(0)
      length = len(sent)

      if length < self.max_batch_size:
        texts.append(sent)
        continue

      # long sentence that cannot be split any more
      if len(texts):
        translated.extend(self.translate_texts(texts, input_data))
        texts = []

      # no translation
      translated.append(sent)

    if len(texts):
      translated.extend(self.translate_texts(texts, input_data))
      
    return (' ' if input_data.target_lang == 'en' else '').join(translated)

  def translate_texts(
      self,
      texts: list[str],
      input_data: ActInputData
  ) -> list[str]:
    """
    Translate texts

    :param texts: List of texts to be translated
    :param input_data: The input data from `process` method
    :return: List of translated texts
    """
    translated: list[str] = []
    
    batch: list[str] = []
    batch_size: int = 0

    while len(texts):
      txt = texts.pop(0)
      length = len(txt)

      if batch_size + length < self.max_batch_size:
        # add to batch
        batch.append(txt)
        batch_size += length
        continue

      if len(batch):
        # translate batch and reset batch
        translated.extend(self.translate_batch(batch, input_data))
        batch, batch_size = [], 0

      if length < self.max_batch_size:
        batch.append(txt)
        batch_size = length
        continue
      
      # long line
      translated.append(self.translate_long_line(txt, input_data))

    if len(batch):
      translated.extend(self.translate_batch(batch, input_data))

    return translated

  async def wait_for_file_translated(self, doc_id: str) -> str:
    """
    Wait for the completion of a file being translated

    :param doc_id: Id of the file being translated
    :return: Id of the translated file
    """
    url = f"{self.api_base_url}/trans/document-progress/"
    timeout = time.time() + self.config.timeout
    retries = self.config.max_retries

    while time.time() < timeout and retries:
      response = requests.post(url, headers=self.post_headers, json={'key': doc_id})

      if response.ok:
        result = response.json()
        if is_act_result_ok(result):
          if result['data']['status'] == 'finished':
            return result['data']['id']
        else:
          log_act_result_error(result)
          retries -= 1
      else:
        log_act_response_error(response)
        retries -= 1

      await asyncio.sleep(5)

    if not retries:
      raise ActTooManyRetriesException(
        self.config.max_retries,
        "Too many errors when waiting for file translation"
      )

    raise TimeoutError("Act file translation is timed out")
  
  def get_file_download_url(self, doc_id: str) -> str:
    """
    Get download url of the translated file

    :param doc_id: Id of the translated file
    :return: The download url
    """
    url = f"{self.api_base_url}/trans/document-download/"

    response = requests.post(url, headers=self.post_headers, json={'progress_key': doc_id, 'type': '2'})

    if response.ok:
      result = response.json()
      if is_act_result_ok(result):
        return result['data']['download_url']
      else:
        raise ActError(log_act_result_error(result))
    else:
      raise ActError(log_act_response_error(response))

  async def translate_file(
      self,
      source_filepath: str,
      input_data: ActInputData
  ) -> str:
    """
    Translate a file

    :param source_filepath: The path of source file to be translated
    :input_data: The input data from `process` method
    :return: The path of translated file
    """
    working_dir = self.config.working_dir

    if not os.path.isdir(working_dir):
      raise ActConfigException(
        f"working_dir",
        "Invalid working_dir: {working_dir}"
      )
    
    if not os.path.isfile(source_filepath):
      raise ValueError(f"{source_filepath} is not a valid file path")
    
    content_type, _ = mimetypes.guess_type(source_filepath)
    content_type = content_type or 'application/octet-stream'

    filename = add_random_suffix_to_filename(os.path.basename(source_filepath))

    data = MultipartEncoder(fields={
      'filename': filename,
      'file': (filename, open(source_filepath, 'rb'), content_type),
      'source_lang': input_data.source_lang,
      'target_lang': input_data.target_lang,
      'domain': 'medical'
    })

    url = f"{self.api_base_url}/trans/document/?team_id={self.config.team_id}"
    retries = self.config.max_retries

    while retries:
      response = requests.post(
        url, headers=self.post_headers | {'Content-Type': data.content_type},
        data=data, timeout=60
      )

      if response.ok:
        result = response.json()
        if is_act_result_ok(result):
          doc_id = await self.wait_for_file_translated(result['data']['id'])
          # Download the translated file
          download_url = f"{self.base_url}{self.get_file_download_url(doc_id)}"
          downloader = Download(DownloadConfig(target_dir=working_dir))
          downloaded = await downloader.process(DownloadInputData(urls=[download_url]))
          return downloaded[0]
        else:
          log_act_result_error(result)
          retries -= 1
      else:
        log_act_response_error(response)
        retries -= 1
    
    raise ActTooManyRetriesException(
      self.config.max_retries,
      "Failed to access ACT's translate_doc service after multiple retries"
    )

  async def process(self, input_data: ActInputData) -> dict[str, list[str]]:
    """Process input data"""
    texts, files = input_data.texts, input_data.files

    if len(texts):
      return {'translated': self.translate_texts(texts, input_data)}
    
    working_dir = self.config.working_dir
    if not os.path.isdir(working_dir):
      raise ActConfigException(
        f"working_dir",
        "Invalid working_dir: {working_dir}"
      )

    tasks = []
    for file in files:
      tasks.append(self.translate_file(file, input_data))

    results = await asyncio.gather(*tasks)
    return {'translated': results}