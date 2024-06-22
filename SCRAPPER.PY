from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
service =Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://leetcode.com/contest/weekly-contest-402/ranking")


anchor_tags = driver.find_elements(By.CSS_SELECTOR, "td a[data-target='#submission']")

# Iterate over each anchor tag and click on it
for anchor_tag in anchor_tags:
    anchor_tag.click()
    time.sleep(2)  # Adjust as needed depending on modal animation and load time

    # Find elements inside the modal (example: modal title)
    #modal_title = driver.find_element(By.CLASS_NAME, "modal-title").text
    #print("Modal title:", modal_title)
    pre_element = driver.find_element(By.CSS_SELECTOR, "pre")
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pre_element)

# Extract the Java code from the <code> element
    java_code = driver.find_element(By.CSS_SELECTOR, "code.cpp.hljs").text

# Print the extracted Java code
    print(java_code)

    # Close the modal (assuming it has a close button)
    close_button = driver.find_element(By.CSS_SELECTOR, "button[data-dismiss='modal']")
    close_button.click()
#text_feild = driver.find_element(By.CLASS_NAME,"java hljs")

print("SDfs")



time.sleep(10)

driver.close()