import feedparser
import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
import hashlib
from utils import load_blacklist, get_hash, save_blacklist, is_blacklisted
from config import DATA_FILE

def load_articles():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_articles(articles):
    with open(DATA_FILE, "w") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

def fetch_and_save(source_url):
    if is_blacklisted(source_url):
        return
    
    articles = load_articles()
    for existing in articles:
        if existing["url"] == source_url:
            return  # уже есть
    
    try:
        feed = feedparser.parse(source_url)
        new_articles = []
        
        for entry in feed.entries[:50]:  # до 50
            title = entry.title
            url = entry.link
            published = entry.get("published", "")
            summary = entry.get("summary", "")
            
            # Полный текст, если в RSS только анонс
            content = summary
            if hasattr(entry, 'content') and entry.content:
                content = entry.content[0].value
            
            # Хэш для дубликатов
            article_hash = get_hash(title + content[:500])
            if any(a.get("hash") == article_hash for a in articles):
                continue
            
            # Скачиваем изображение (если есть)
            image_url = None
            if "media_content" in entry:
                image_url = entry.media_content[0].get("url", "")
            elif "thumbnail" in entry:
                image_url = entry.thumbnail
            
            new_articles.append({
                "title": title,
                "url": url,
                "content": content,
                "image_url": image_url,
                "published": published,
                "hash": article_hash,
                "status": "New"
            })
        
        if new_articles:
            articles.extend(new_articles)
            save_articles(articles)
            save_blacklist(load_blacklist() + [source_url])
    except Exception as e:
        print(f"Ошибка {source_url}: {e}")
