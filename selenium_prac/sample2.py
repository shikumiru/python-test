from selenium import webdriver
import chromedriver_binary

options = webdriver.ChromeOptions()
options.add_argument('--headless')

print('connecting to remote browser...')
driver = webdriver.Chrome()

driver.get('https://python.org')
print(driver.current_url)

driver.quit()