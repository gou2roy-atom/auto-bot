from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://zefame.com/en/free-instagram-views"
PROFILE_LINK = "https://www.instagram.com/reel/DW2xRi0iVU8/?igsh=ZDBqYW02amVsNjk2"

def run_bot():
    driver = webdriver.Chrome()

    while True:
        try:
            print("Opening page...")
            driver.get(URL)

            time.sleep(5)

            print("Finding input field...")
            input_box = driver.find_element(By.TAG_NAME, "input")
            input_box.clear()
            input_box.send_keys(PROFILE_LINK)

            print("Clicking button...")
            button = driver.find_element(By.XPATH, "//button[contains(text(),'Get Now')]")
            button.click()

            print("Waiting 7 minutes...")
            time.sleep(420)

            print("Refreshing...")
            driver.refresh()

        except Exception as e:
            print("Error:", e)
            driver.refresh()
            time.sleep(10)

run_bot()
