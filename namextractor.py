from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service =Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
username = "mhasan01"
for i in range(1,1024):
    driver.get(f"https://leetcode.com/contest/weekly-contest-402/ranking/{i}")
    time.sleep(5)
    

        # Wait for the table to load (adjust wait time as necessary)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'tr')))

        # Find all rows in the table
    rows = driver.find_elements(By.TAG_NAME, 'tr')

        # Iterate through each row
    for row in rows:
            # Extract username
        username_element = row.find_element(By.CLASS_NAME, 'ranking-username')
        username = username_element.text.strip()

            # Find the anchor tag for code submission and click it
        code_anchor = row.find_element(By.CSS_SELECTOR, "td:nth-child(5) aa[data-target='#submission']")
        code_anchor.click()

            # Handle the code modal (not implemented here, depends on your specific needs)

            # Optionally print username for verification
        print(f"Clicked on code for: {username}")

    

                # Close the modal (assuming it has a close button)
                
