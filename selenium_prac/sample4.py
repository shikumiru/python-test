import time
import chromedriver_binary
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_check_google_translate_work_properly():
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.jp")
    
    time.sleep(3)
    
    input_search = driver.find_element(By.XPATH, "//*[@id='APjFqb']")
    input_search.clear()
    input_search.send_keys('翻訳')
    input_search.submit()
    
    time.sleep(3)
    
    link_list = driver.find_element(By.PARTIAL_LINK_TEXT, "Google 翻訳")
    link_list.click()
    
    time.sleep(3)
    
    input_text = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea")
    input_text.send_keys("america")
    input_text.send_keys(Keys.ENTER)
    
    time.sleep(3)
    
    output_text = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div/div[6]/div/div[1]/span[1]/span/span")
    assert output_text.text == 'アメリカ'
    
    driver.quit()