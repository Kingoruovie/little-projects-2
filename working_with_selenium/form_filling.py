from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/home/ovie/Documents/PROGRAMS/chromedriver/chromedriver"
site_url = "http://secure-retreat-92358.herokuapp.com/"

service = Service(chrome_driver_path)
newsletter_driver = webdriver.Chrome(service=service)

newsletter_driver.get(site_url)
first_name = newsletter_driver.find_element(by=By.NAME, value="fName")
first_name.send_keys("Ovie")
last_name = newsletter_driver.find_element(by=By.NAME, value="lName")
last_name.send_keys("Oru")
email = newsletter_driver.find_element(by=By.NAME, value="email")
email.send_keys("pythontrialg@gmail.com")

sign_up_button = newsletter_driver.find_element(by=By.CSS_SELECTOR,
                                                value=".btn")
sign_up_button.click()
