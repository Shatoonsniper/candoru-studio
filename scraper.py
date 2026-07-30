import feedparser
import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
import hashlib

BLACKLIST_FILE = "blacklist.json"

def load_blacklist():
    if os.path.exists(BLACKLIST_FILE):
        with open(BLACKLIST_FILE, "r") as f:
            return json.load(f)
    return []

def save_blacklist(blacklist):
    with open(BLACKLIST_FILE, "w") as f:
        json.dump(blacklist, f, ensure_ascii=False)

def fetch_and_save(source_url):
    # Проверка дубликатов + Blacklist
    # ... (полный код с feedparser + BeautifulSoup + hash заголовка)
    # Если материал уже есть — пропускаем
    # Если полный текст не в RSS — скачиваем со страницы
