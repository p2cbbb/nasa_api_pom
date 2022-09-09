import os
import requests

api_dev_key = os.environ.get('PASTEBIN_API_KEY')


def get_nasa_image_json(url):
    """функция для получения ссылки на изображение и описания картинки с помощью api"""
    img_json = requests.get(url).json()
    img_hdurl = img_json.get('hdurl')
    img_explanation = img_json.get('explanation')
    return img_hdurl, img_explanation


def create_pastebin_note(api_dev_key, text):
    """функция для создания заметки на сайте pastebin.com с помощью api"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        "api_dev_key": api_dev_key,
        "api_paste_code": text,
        "api_option": "paste",
        "api_paste_expire_date": "1W",
        "api_paste_private": "0"
    }
    response = requests.post("https://pastebin.com/api/api_post.php", headers=headers, data=data)
    return response.content


