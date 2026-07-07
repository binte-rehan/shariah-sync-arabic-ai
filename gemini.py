import google.generativeai as genai
from config import GEMINI_API_KEY,MODEL_NAME
from prompts import SYSTEM_PROMPT
genai.configure(api_key=GEMINI_API_KEY)
model=genai.GenerativeModel(MODEL_NAME)
def ask_ai(question:str)->str:
    try:
        r=model.generate_content(SYSTEM_PROMPT+"\n\n"+question)
        return getattr(r,"text","No response")
    except Exception as e:
        return f"Error: {e}"
