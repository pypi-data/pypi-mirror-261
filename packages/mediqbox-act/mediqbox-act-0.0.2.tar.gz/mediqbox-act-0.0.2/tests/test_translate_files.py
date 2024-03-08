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

def test_translate_files():
  data_dir = os.path.join(os.path.dirname(__file__), 'data')
  files = [os.path.join(data_dir, item) for item in ['en.txt', 'en.pdf']]

  act.ac.config.working_dir = os.path.join(os.path.dirname(__file__), 'test_results')

  result = act.process(ActInputData(
    files=files,
    source_lang = 'en',
    target_lang = 'zh'
  ))

  assert result.get('translated') and len(result['translated']) == 2

  print(result)

if __name__ == '__main__':
  test_translate_files()