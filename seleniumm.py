from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

VALID_EMAIL    = "vanshalnagar@gmail.com"
VALID_PASSWORD = "van2005"
INVALID_EMAIL    = "23bcp038@sot.pdpu.ac.in"
INVALID_PASSWORD = "van2005"
URL = ""

def login(driver, email, password):
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-btn").click()

def test_valid_login(driver):
    print("\n--- Testing Valid Login ---")
    login(driver, VALID_EMAIL, VALID_PASSWORD)

    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.visibility_of_element_located((By.ID, "dashboard")))
        print("Login Successful!")
    except Exception:
        print("Login Failed — dashboard not found.")

def test_invalid_login(driver):
    print("\n--- Testing Invalid Login ---")
    login(driver, INVALID_EMAIL, INVALID_PASSWORD)
    wait = WebDriverWait(driver, 10)
    try:
        error = wait.until(EC.visibility_of_element_located((By.ID, "error-msg")))
        print(f"Invalid Credentials Message: {error.text}")
    except Exception:
        print("No error message displayed.")
driver = webdriver.Edge()
driver.maximize_window()

try:
    test_valid_login(driver)
    test_invalid_login(driver)
finally:
    driver.quit()
    print("\nBrowser closed.")
