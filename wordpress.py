import requests
from dotenv import load_dotenv
import os
import base64
from PIL import Image
import io

load_dotenv()

def publish_to_wordpress(title, content, image_url=None, existing_post_id=None):
    url = f"{os.getenv('WORDPRESS_URL')}/wp-json/wp/v2/posts"
    auth = (os.getenv('WORDPRESS_USER'), os.getenv('WORDPRESS_APP_PASSWORD'))
    
    data = {
        "title": title,
        "content": content,
        "status": "draft" if existing_post_id else "publish",
        "meta": {"wp:featuredmedia": image_id} if image_id else {}
    }
    
    response = requests.post(url, json=data, auth=auth)
    
    if response.status_code == 201:
        return {"success": True, "id": response.json()["id"]}
    
    return {"success": False, "error": response.text}
