import time
from src.config import load_config
from src.scraper import fetch_and_save

def worker():
    while True:
        for source in load_config()["sources"]:
            fetch_and_save(source)
        time.sleep(900)  # 15 минут

if __name__ == "__main__":
    worker()
