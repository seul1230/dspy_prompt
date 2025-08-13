import dspy

class MathQASignature(dspy.Signature):
    """주어진 수학 지시문에 대해 풀이 과정을 설명하고 최종 답을 응답"""
    instruction = dspy.InputField(desc="수학 문제에 대한 지시문")
    reasoning_steps = dspy.OutputField(desc="풀이 과정. '1단계: 1 + 1 = 2\\n' 형식")
    final_answer = dspy.OutputField(desc="정답")

class Assess(dspy.Signature):
    """모델의 응답을 평가"""
    assessed_text = dspy.InputField(desc="평가 대상 텍스트")
    assessment_question = dspy.InputField(desc="평가 질문")
    assessment_answer = dspy.OutputField(desc="예/아니오")
