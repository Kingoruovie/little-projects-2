from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

chrome_driver_path = "C:/Users/Ovie/Documents/PROGRAMS/chromedriver/chromedriver.exe"
site_url = "http://orteil.dashnet.org/experiments/cookie/"

service = Service(chrome_driver_path)
cookie_driver = webdriver.Chrome(service=service)

cookie_driver.get(site_url)

cookie_money = cookie_driver.find_element(by=By.ID, value="money")
print(cookie_money.text)

# Stuffs to buy to increase productivity of cookie clicking
cookie_cursor = cookie_driver.find_element(by=By.CSS_SELECTOR, value="#buyCursor b")

cookie_grandma = cookie_driver.find_element(by=By.CSS_SELECTOR, value="#buyGrandma b")

cookie_factory = cookie_driver.find_element(by=By.CSS_SELECTOR, value="#buyFactory b")

cookie_mine = cookie_driver.find_element(by=By.CSS_SELECTOR, value="#buyMine b")

cookie_shipment = cookie_driver.find_element(by=By.CSS_SELECTOR, value="#buyShipment b")

cookie_lab = cookie_driver.find_element(by=By.CSS_SELECTOR, value="#buyAlchemy\ lab b")
print(cookie_lab.text)
cookie_portal = cookie_driver.find_element(by=By.CSS_SELECTOR, value="#buyPortal b")

cookie_machine = cookie_driver.find_element(by=By.CSS_SELECTOR, value="#buyTime\ machine b")
cookie_machine_list = cookie_machine.text.split("-")
print(cookie_machine_list)

cookie = cookie_driver.find_element(by=By.ID, value="cookie")

time = datetime.now()
minute_delta = timedelta(seconds=30)
new_time = time + minute_delta

should_click = True

while should_click:
    cookie.click()
    if datetime.now().second == new_time.second:
        should_click = False
