import openai
from dotenv import load_dotenv
import os

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENROUTER_API_KEY"))

def process_article(original_text, original_title):
    # AI-рейт на русском, без добавления фактов
    prompt = f"""Рерайт оригинальной статьи в уникальный текст на русском языке без добавления неподтверждённых фактов:
    
    Заголовок: {original_title}
    Текст: {original_text}
    
    Верни только Markdown с заголовками, абзацами и списками."""
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    rewrite = response.choices[0].message.content

    # Генерация SEO
    seo_prompt = f"Сгенерируй: SEO-заголовок, meta description, латинский slug, список тегов для заголовка '{original_title}'"
    seo = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": seo_prompt}],
        temperature=0.3
    )
    return rewrite, seo.choices[0].message.content
