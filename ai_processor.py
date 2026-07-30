import openai
from dotenv import load_dotenv
import os

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENROUTER_API_KEY"))

def process_article(original_text, original_title):
    # AI-рейт
    prompt = f"""Рерайт оригинальной статьи в уникальный текст на русском языке без добавления неподтверждённых фактов. 
Заголовок: {original_title}
Текст: {original_text[:2000]}"""
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    rewrite = response.choices[0].message.content

    # SEO
    seo_prompt = f"Сгенерируй для заголовка '{original_title}': SEO-заголовок, meta description (максимум 160 символов), латинский slug, список тегов (через запятую)"
    seo_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": seo_prompt}],
        temperature=0.3
    )
    seo = seo_response.choices[0].message.content

    return rewrite, seo
