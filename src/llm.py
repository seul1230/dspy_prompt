import dspy
from .config import get_openai_api_key

def configure_lm(model_name: str = "gpt-4o-mini", temperature: float = 0.0):
    api_key = get_openai_api_key()
    lm = dspy.LM(model=model_name, api_key=api_key, temperature=temperature)
    dspy.settings.configure(lm=lm)
    return lm
