from time import sleep
from selenium.webdriver.common.by import By

def test_title_good(driver, url):
    driver.get(url)
    title = driver.find_element(By.TAG_NAME, 'h1')
    
    assert title.text == "国土を測る・描く・守る・伝える", "タイトルが不正です"
    return

def test_title_bad(driver, url):
    driver.get(url)
    title = driver.find_element(By.TAG_NAME, 'h1')
    
    assert title.text == "国土を測る・書く・守る・伝える", "タイトルが不正です"
    return

if __name__ == "__main__":
    test_title_good()