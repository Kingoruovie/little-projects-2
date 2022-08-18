from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/home/ovie/Documents/PROGRAMS/chromedriver/chromedriver"

service = Service(chrome_driver_path)
wiki_driver = webdriver.Chrome(service=service)

wiki_driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_stat = wiki_driver.find_element(by=By.CSS_SELECTOR, value=("#articlecount a"))
# article_stat.click()

all_portals = wiki_driver.find_element(by=By.LINK_TEXT, value="Wikibooks")
all_portals.click()