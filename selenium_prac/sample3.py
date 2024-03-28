from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_binary

driver = webdriver.Chrome()

driver.get('https://python.org')
print(driver.current_url)

search_field = driver.find_element(By.ID, "id-search-field")
search_field.click()
search_field.clear()
search_field.send_keys("list")
go_button = driver.find_element(By.ID, "submit")
go_button.click()
time.sleep(1)
print(driver.current_url)

list_comprehension_links = driver.find_elements(By.XPATH, "//ul[@class='list-recent-eventsmenu']/li[13]//a")

if list_comprehension_links:
    for link in list_comprehension_links:
        print(link.get_attribute('href'))
else:
    print("No links found")

driver.quit()