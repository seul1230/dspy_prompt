import cloudpickle
from pathlib import Path

from .llm import configure_lm
from .modules import GenerateAnswer

COMPILED_PATH = "compiled_program.pkl"

def load_compiled_or_fallback():
    """컴파일된 프로그램이 있으면 로드, 없으면 기본 모듈 사용"""
    if Path(COMPILED_PATH).exists():
        with open(COMPILED_PATH, "rb") as f:
            return cloudpickle.load(f)
    return GenerateAnswer()

def run_once(instruction: str):
    model = configure_lm()  # LLM 설정
    program = load_compiled_or_fallback()
    pred = program(instruction=instruction)
    print("Question:", instruction)
    print("Reasoning Steps:", pred.reasoning_steps)
    print("Final Answer:", pred.final_answer)
    
    print(model.inspect_history(n=1))

if __name__ == "__main__":
    # 예시 실행
    run_once("(3-5)*3+1=?")
    
