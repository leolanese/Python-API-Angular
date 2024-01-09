from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://127.0.0.1:8000/"

driver = webdriver.Chrome()
driver.get(url)

body_element = driver.find_element(By.TAG_NAME, "body")

if "API Server root - http://localhost:8000/" in body_element.text:
    print("Text found on the page.")
else:
    print("Text not found on the page.")

# Close the browser
driver.quit()
