import openai
import os
from dotenv import load_dotenv

load_dotenv()  # .env dosyasından API anahtarını al

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_answer(question):
    prompt = f"""Sen bir üniversite hocasının yapay zekâ destekli asistanısın. 
    Öğrencilerin dersle ilgili sorularını kısa ve net şekilde yanıtlıyorsun. 
    Soru: {question}
    Cevap:"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Sen üniversite dersleriyle ilgili soruları yanıtlayan bir yapay zekâ asistanısın."},
                {"role": "user", "content": question}
            ],
            temperature=0.5,
            max_tokens=200
        )
        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"⚠️ Bir hata oluştu: {e}"
