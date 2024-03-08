import logging
import os
import random
import re
import string

from requests import Response
from typing import Literal
  
def is_act_result_ok(result: dict) -> bool:
  return isinstance(result, dict) and result.get('errcode') == 0

def texts_to_act_lines(texts: list[str]) -> list[dict[str, int|str]]:
  return [{'id': i, 'text': texts[i]} for i in range(len(texts))]

def act_lines_to_texts(lines: list[dict[str, int|str]]) -> list[str]:
  return [line['text'] for line in lines]

def split_sentences(paragraph: str, lang: Literal['en', 'zh']='en') -> list[str]:
  if lang == 'en':
    return re.split(r'(?<=[.!?]) +', paragraph)
  
  if lang == 'zh':
    sentences = re.split(r'(?<=[。？！])', paragraph)
    return [sentence.strip() for sentence in sentences if sentence.strip()]
  
def add_random_suffix_to_filename(filename: str, length: int=6) -> str:
  suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
  base_name, ext = os.path.splitext(filename)
  return f"{base_name}-{suffix}{ext}"

def log_act_result_error(result: dict):
  message = f"ACT result error: {result['msg']}"
  logging.error(f"ACT result error: {message}")
  return message

def log_act_response_error(response: Response):
  message = f"ACT response error(status_code {response.status_code}): {response.reason}"
  logging.error(message)
  return message