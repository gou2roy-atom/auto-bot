from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# ===== CONFIG =====
URL = "https://zefame.com/en/free-instagram-views"
PROFILE_LINK = "https://www.instagram.com/reel/DW2xRi0iVU8/?igsh=ZDBqYW02amVsNjk2"
WAIT_TIME = 420  # 7 minutes

# ===== SETUP DRIVER =====
def create_driver():
    chrome_options = Options()
    
    # Headless mode for GitHub
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    return driver


# ===== MAIN BOT FUNCTION =====
def run_bot():
    driver = create_driver()
    wait = WebDriverWait(driver, 20)

    try:
        print("🔵 Opening page...")
        driver.get(URL)

        # Wait for input field (better than sleep)
        print("🟡 Waiting for input field...")
        input_box = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )

        # Clear and enter profile link
        input_box.clear()
        input_box.send_keys(PROFILE_LINK)
        print("🟢 Profile link entered")

        # Wait and click button
        print("🟡 Waiting for button...")
        button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Get Now')]"))
        )

        button.click()
        print("🟢 Button clicked")

        # Wait 7 minutes
        print("⏳ Waiting 7 minutes...")
        time.sleep(WAIT_TIME)

        print("✅ Cycle completed successfully")

    except Exception as e:
        print("❌ ERROR:", str(e))
        sys.exit(1)

    finally:
        driver.quit()
        print("🔴 Browser closed")


# ===== RUN =====
if __name__ == "__main__":
    run_bot()
