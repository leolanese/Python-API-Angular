from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://127.0.0.1:8000/"
expected_text = "API Server root - http://localhost:8000/"

driver = webdriver.Chrome()
driver.get(url)

body_element = driver.find_element(By.TAG_NAME, "body")

if expected_text in body_element.text:
    print(f"Success: Text '{expected_text}' found on the page.")
else:
    print(f"Error: Text '{expected_text}' not found on the page.")

driver.quit()
