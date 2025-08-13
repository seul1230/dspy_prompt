import dspy
from .signatures import MathQASignature

class GenerateAnswer(dspy.Module):
    def __init__(self):
        super().__init__()
        self.CoT = dspy.ChainOfThought(MathQASignature)

    def forward(self, instruction: str):
        prediction = self.CoT(instruction=instruction)
        return dspy.Prediction(
            reasoning_steps=prediction.reasoning_steps,
            final_answer=prediction.final_answer
        )
