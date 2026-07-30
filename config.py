import json
import os
from dotenv import load_dotenv

load_dotenv()

DATA_FILE = "sources.json"

def load_config():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"sources": []}

def save_config(config):
    with open(DATA_FILE, "w") as f:
        json.dump(config, f, ensure_ascii=False)

# Пример .env
if os.getenv("OPENROUTER_API_KEY"):
    pass  # AI ключ
