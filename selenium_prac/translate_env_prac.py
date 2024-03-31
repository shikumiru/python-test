import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()
DRIVER_PATH = os.getenv("DRIVER_PATH")

print("翻訳したい言葉を入力：")
word = input()
print("翻訳後の言語の言語コードを入力 (例: 英語 -> en, 日本語 -> ja)：")
translation_language_code = input()

chrome_service = ChromeService(executable_path=DRIVER_PATH)
chrome_options = ChromeOptions()
chrome_options.add_argument("--lang=ja")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get("https://translate.google.com/")

time.sleep(3)

input_text = driver.find_element(By.XPATH, '//textarea[@aria-label="原文"]')
input_text.send_keys(word)

time.sleep(3)

element = driver.find_element(By.XPATH, '//*[@id="i15"]')
selected_language_code = element.get_attribute("data-language-code")

if selected_language_code != translation_language_code:
    choice_language = driver.find_element(By.XPATH, f'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/div/div[2]/div/div//button[@data-language-code="{translation_language_code}"]')
    choice_language.click()

time.sleep(3)

output_text = driver.find_element(By.XPATH, '//span[@class="ryNqvb"]')
print("翻訳結果：", output_text.text)

driver.quit()