import os
from dotenv import load_dotenv

# .env 로드 (루트에서 실행 시 자동 탐색)
load_dotenv()

def get_openai_api_key() -> str:
    key = os.getenv("OPENAI_KEY")
    if not key:
        raise RuntimeError("OPENAI_KEY가 설정되어 있지 않습니다. .env 파일을 확인하세요.")
    return key
