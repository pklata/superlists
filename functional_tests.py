from selenium import webdriver

DEVELOPMENT_URL = "http://127.0.0.1:8000/"

browser = webdriver.Firefox()
browser.get(f'{DEVELOPMENT_URL}')

assert "Django" in browser.title
