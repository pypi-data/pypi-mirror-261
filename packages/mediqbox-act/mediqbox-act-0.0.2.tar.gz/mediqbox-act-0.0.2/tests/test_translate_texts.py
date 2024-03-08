import os
from dotenv import load_dotenv

from mediqbox.abc.async2sync import Async2Sync
from mediqbox.act.act import (
  Act,
  ActConfig,
  ActInputData
)

load_dotenv()

from tests.settings import settings

act = Async2Sync(Act(config=ActConfig(
  username=settings.ACT_USERNAME,
  password=settings.ACT_PASSWORD
)))

act.ac.login()

def test_translate_simple_text():
  texts = ["Hello, world!"]

  result = act.process(ActInputData(
    texts = texts,
    source_lang = 'en',
    target_lang = 'zh'
  ))

  assert result.get('translated') and len(result['translated']) == 1

  print(result)

def test_translate_long_line():
  filename = os.path.join(
    os.path.dirname(__file__),
    'data', 'en_long_line.txt'
  )

  with open(filename, 'r') as fp:
    long_line = fp.readline().strip()

  result = act.process(ActInputData(
    texts = [long_line],
    source_lang = 'en',
    target_lang = 'zh'
  ))

  assert (result.get('translated') and
          len(result['translated']) == 1 and
          not result['translated'][0].strip() == long_line)
  
  print(result)
  
if __name__ == '__main__':
  # test_translate_simple_text()
  test_translate_long_line()