from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def Webdriver(headless):
    options = Options()
    if headless:
        options.add_argument('--headless')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    PATH = 'C:\Program Files\chromedriver.exe'
    s = Service(PATH)
    driver = webdriver.Chrome(service=s, options=options)
    return driver
    ...
