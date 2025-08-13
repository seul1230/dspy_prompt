import dspy
from .signatures import Assess

def metric(example, pred, trace=None):
    """정답 일치 + 형식 준수(둘 다 충족 시 2점, 아니면 0점)"""
    answer, reasoning_steps = example.final_answer, pred.reasoning_steps

    # 평가 질문
    correct_q = f"최종 답변이 '{answer}'와 일치하는가? (예/아니오)"
    formatting_q = "풀이 과정이 형식을 준수하는가? (예/아니오)"

    # 평가 실행
    correct_res = dspy.Predict(Assess)(assessed_text=reasoning_steps, assessment_question=correct_q)
    formatting_res = dspy.Predict(Assess)(assessed_text=reasoning_steps, assessment_question=formatting_q)

    correct_bool = (correct_res.assessment_answer or "").strip() == "예"
    formatting_bool = (formatting_res.assessment_answer or "").strip() == "예"

    score = (correct_bool + formatting_bool) if (correct_bool and formatting_bool) else 0

    if trace is not None:
        return score >= 2  # 최적화 플래그
    return score / 2.0     # 0 또는 1 반환
