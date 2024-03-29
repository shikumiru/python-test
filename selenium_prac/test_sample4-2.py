import time
from selenium.webdriver.common.by import By

def test_check_google_translate_work(driver):
    driver.get("https://translate.google.com/")
    
    time.sleep(3)
    
    input_text = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
    input_text.send_keys("japan")
    
    time.sleep(3)
    
    output_text = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div/div[6]/div/div[1]/span[1]/span/span')
    assert output_text.text == "日本"
    return

if __name__=="__main__":
    test_check_google_translate_work()