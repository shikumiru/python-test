import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://translate.google.com/")

time.sleep(3)

input_text = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
input_text.send_keys("パターン")

time.sleep(3)

choice_english = driver.find_element(By.XPATH, '//*[@id="i16"]/span[3]')
choice_english.click()

time.sleep(3)

output_text = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div/div[6]/div/div[1]/span[1]/span/span')
print(output_text.text)

driver.quit()