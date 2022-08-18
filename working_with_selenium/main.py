from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Ovie/Documents/PROGRAMS/chromedriver/chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.python.org/")
time_list_of_upcoming_events = driver.find_elements(by=By.CSS_SELECTOR, value=(
    ".event-widget div ul li time"))
name_list_of_upcoming_event = driver.find_elements(by=By.CSS_SELECTOR, value=(
    ".event-widget div ul li a"))

events_dict = {}

for i in range(0, 5):
    events_dict[i] = {
        "time": f"{time_list_of_upcoming_events[i].text}",
        "name": f"{name_list_of_upcoming_event[i].text}"
        }

print(events_dict)
driver.close()
