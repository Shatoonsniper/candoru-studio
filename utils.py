import hashlib
import json
import os

BLACKLIST_FILE = "blacklist.json"

def load_blacklist():
    if os.path.exists(BLACKLIST_FILE):
        with open(BLACKLIST_FILE, "r") as f:
            return json.load(f)["urls"]
    return []

def save_blacklist(urls):
    with open(BLACKLIST_FILE, "w") as f:
        json.dump({"urls": urls}, f, ensure_ascii=False)

def get_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def is_blacklisted(url):
    return url in load_blacklist()
