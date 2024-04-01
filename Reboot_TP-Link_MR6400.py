from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Go to the TP-Link router's web interface
driver.get('URL-ROUTER')

# Wait for the page to load, then find the password field
password = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.ID, 'pc-login-password')))

# Enter the default password
password.send_keys('PASSWORD-ROUTER')

# Find the login button and click it
login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'pc-login-btn')))
login_button.click()

# Kalau sudah pernah login auto klik yes untuk konfirmasi login
confirmlogin_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'confirm-yes')))
driver.execute_script("arguments[0].click();", confirmlogin_button)

# Wait for the page to load, then find the reboot button by its ID and click it
reboot_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'topReboot')))
driver.execute_script("arguments[0].click();", reboot_button)

# Wait for the page to load, then find the confirmation button by its class and click it
confirmreboot_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-button.green.pure-button.btn-msg.btn-msg-ok.btn-confirm')))
confirmreboot_button.click()

# Handle the confirmation alert
try:
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
except NoAlertPresentException:
    print("No alert present")

# Close the browser
driver.quit()

