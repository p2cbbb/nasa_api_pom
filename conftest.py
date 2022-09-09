import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    browser = None
    print("\nstart chrome browser for test..")
    options = Options()
    options.add_argument("--disable-notifications")
    options.page_load_strategy = 'normal'
    browser = webdriver.Chrome(options=options, executable_path=r"C:\chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()