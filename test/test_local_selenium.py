from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://127.0.0.1:8000/"

# Use a webdriver (make sure to have the appropriate driver installed, e.g., chromedriver)
driver = webdriver.Chrome()
driver.get(url)

# Find the text inside the body tag
body_element = driver.find_element(By.TAG_NAME, "body")

# Check if the desired text is present in the body
if "API Server root - http://localhost:8000/" in body_element.text:
    print("Text found on the page.")
else:
    print("Text not found on the page.")

# Close the browser
driver.quit()
