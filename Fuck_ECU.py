from turtle import title
from initdriver import Webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import polling2
from nameGen import nameGen
import random
import time

driver = Webdriver(False)


def run(driver):
    driver.get(
        'https://docs.google.com/forms/d/e/1FAIpQLSdJf-QRqH7JmtzrkwPId2Vth3pteB90KYNnqeYpz_hO6i4_ug/viewform')
    start = time.time()
    print(driver.title)
    driver.implicitly_wait(10)
    inputs = driver.find_elements(By.CSS_SELECTOR, 'input.whsOnd')
    textAreas = driver.find_elements(By.CSS_SELECTOR, 'textArea.KHxj8b.tL9Q4c')
    submitButton = driver.find_element(
        By.CSS_SELECTOR, 'span.NPEfkd.RveJvd.snByac')
    submit(inputs, textAreas, submitButton)
    stop = time.time() - start
    print(stop)
    # driver.close()
    ...


def createInputs():
    names = nameGen()
    # print(names['first'], names['last'])
    year = random.randrange(18, 23)
    email = (f'{names["last"][0:7]}{names["first"][0]}{year}@ecu.edu')
    entre = 'Elias Tewolde'
    dontputthatshiton = 'TJ Supreme '  # !
    musicartist = 'Naroid'
    visualartist = 'Manoah Tsegai'
    greek = 'SBC'  # !
    dressedMale = 'Jordan Brown'
    dressedFemale = 'Yom Kongdok'
    impact = 'Diamonds'
    lit = 'SBC-Project 252'
    clown = 'Javeon Dunn'
    athlete = 'Javon Wells'
    bromance = 'Javon Wells & Devin Wallace'
    catfish = 'Briah Pack'  # !
    late = 'Jordan Brown'
    famous = 'Kiana Denison'
    mr = 'Javon Wells'  # !
    mrs = 'Kiana Denison'
    inputText = [email, entre, dontputthatshiton, musicartist, visualartist, dressedMale,
                 dressedFemale, impact, lit, clown, athlete, bromance, catfish, late, famous, mr]
    textAreaText = [greek, mrs]
    return inputText, textAreaText
    ...


def submit(inputs, textAreas, submitButton):
    [li1, li2] = createInputs()

    for (input, ele) in zip(inputs, li1):
        input.send_keys(ele)
        ...

    for textArea, ele in zip(textAreas, li2):
        textArea.send_keys(ele)
        ...

    submitButton.click()
    return
    ...


run(driver)
for i in range(1000):
    ...
