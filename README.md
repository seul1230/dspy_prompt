# DSPy를 이용한 프롬프트 자동 최적화

> DSPy 프레임워크를 활용해 LLM 기반 애플리케이션을 개발하고, 다양한 실험을 진행합니다. 

DSPy는 프롬프트 자동 최적화와 구성 모듈화를 통해, 복잡한 LLM 파이프라인을 안정적이고 재사용 가능하게 만드는 Python 라이브러리입니다.

<br>

### 🧪 완료된 실험

- 수학 질의 응답 MathQA
  - Signature로 입력과 출력 형식을 정의
  - Chain-of-Thought(CoT) 방식으로 reasoning steps와 최종 답안 생성
  - BootstrapFewShot을 활용해 예시 기반 모델 최적화

- 진행 예정
  - DSPy에 Langchain Tool 연동


### 📂 폴더 구조

```bash
src/
├─ config.py         # 환경변수 로드
├─ llm.py            # LLM 설정
├─ signatures.py     # Signature 정의
├─ modules.py        # DSPy 모듈 정의
├─ data.py           # 예시 데이터
├─ metrics.py        # 평가 지표
├─ train.py          # 모델 학습/컴파일
└─ infer.py          # 추론 실행
```

<br>

### ⚙️ 실행 방법

```bash
pip install -r requirements.txt
python -m src.train   # 학습
python -m src.infer   # 추론
```
