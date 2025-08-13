import dspy

# 학습용 예시
trainset = [
    dspy.Example(
        instruction="7과 8을 곱한 뒤, 5를 더하세요.",
        reasoning_steps="1단계: 7 × 8 = 56\n2단계: 56 + 5 = 61",
        final_answer="61"
    ).with_inputs("instruction"),
    dspy.Example(
        instruction="15에서 9를 뺀 다음, 4를 곱하세요.",
        reasoning_steps="1단계: 15 - 9 = 6\n2단계: 6 × 4 = 24",
        final_answer="24"
    ).with_inputs("instruction"),
    dspy.Example(
        instruction="6을 세 번 더한 값에 2를 곱하세요.",
        reasoning_steps="1단계: 6 + 6 + 6 = 18\n2단계: 18 × 2 = 36",
        final_answer="36"
    ).with_inputs("instruction"),
    dspy.Example(
        instruction="12를 3으로 나눈 뒤, 거기에 7을 더하세요.",
        reasoning_steps="1단계: 12 ÷ 3 = 4\n2단계: 4 + 7 = 11",
        final_answer="11"
    ).with_inputs("instruction"),
    dspy.Example(
        instruction="5와 9를 더한 다음, 그 결과에 2를 빼세요.",
        reasoning_steps="1단계: 5 + 9 = 14\n2단계: 14 - 2 = 12",
        final_answer="12"
    ).with_inputs("instruction"),
]

# 개발(검증)용 예시
devset = [
    dspy.Example(
        instruction="9와 4를 더한 뒤, 6을 곱하세요.",
        reasoning_steps="1단계: 9 + 4 = 13\n2단계: 13 × 6 = 78",
        final_answer="78"
    ).with_inputs("instruction"),
    dspy.Example(
        instruction="20을 5로 나눈 다음, 3을 더하세요.",
        reasoning_steps="1단계: 20 ÷ 5 = 4\n2단계: 4 + 3 = 7",
        final_answer="7"
    ).with_inputs("instruction"),
    dspy.Example(
        instruction="10에서 3을 뺀 후, 그 결과를 2로 나누세요.",
        reasoning_steps="1단계: 10 - 3 = 7\n2단계: 7 ÷ 2 = 3.5",
        final_answer="3.5"
    ).with_inputs("instruction"),
]
