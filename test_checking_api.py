from .api import API_DEV_KEY
from .api import get_nasa_image_json, create_pastebin_note
from .pages.note_page import NotePage


def test_create_note_with_api(browser):
    img_description = get_nasa_image_json("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2020-01-01")[1]
    note_url = create_pastebin_note(API_DEV_KEY, img_description).decode("utf-8")
    print(note_url)
    page = NotePage(browser, note_url)
    page.open()
    page.checking_note_text()




