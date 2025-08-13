import cloudpickle
import dspy
from dspy.teleprompt import BootstrapFewShot

from .llm import configure_lm
from .modules import GenerateAnswer
from .data import trainset
from .metrics import metric

OUT_PATH = "compiled_program.pkl"

def main():
    # LLM 설정
    model=configure_lm()
    
    print(f"[OK] Configure LM")

    # 텔레프롬프터로 Few-Shot 컴파일
    teleprompter = BootstrapFewShot(metric=metric)
    compiled_program = teleprompter.compile(GenerateAnswer(), trainset=trainset)

    # 디스크에 저장 (간단히 pickle)
    with open(OUT_PATH, "wb") as f:
        cloudpickle.dump(compiled_program, f)

    print(f"[OK] Compiled program saved to {OUT_PATH}")
    

if __name__ == "__main__":
    main()
