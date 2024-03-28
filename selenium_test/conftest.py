import pytest
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome import service as chrome_fs
from selenium.webdriver.chrome.options import Options as ChromeOptions
from dotenv import load_dotenv

@pytest.fixture(scope="session")
def driver():
    load_dotenv()
    print("start loading driver")
    DRIVER_PATH = os.getenv("DRIVER_PATH")
    assert DRIVER_PATH is not None, "driver path is not given."
    assert Path(DRIVER_PATH).exists(), "driver file does not exist."
    assert Path(DRIVER_PATH).is_absolute(), "driver path must be given as absolute path."
    
    BROWSER_TYPE = os.getenv("BROWSER_TYPE")
    if BROWSER_TYPE == "chrome":
        browser_service = chrome_fs.Service(executable_path=DRIVER_PATH)
        options = ChromeOptions()
    else:
        print("warning: BROWSER_TYPE is not set, continueing test with Chrome driver.")
        browser_service = chrome_fs.Service(executable_path=DRIVER_PATH)
    
    print(os.getenv("IS_HEADLESS"))
    
    IS_HEADLESS = bool(int(os.getenv("IS_HEADLESS")))
    if IS_HEADLESS:
        print("continue in headless mode.")
        options.add_arugment("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-desktop-notifications")
        options.add_argument("--disable-extensions")
    options.add_argument("--lang=ja")
    
    driver = webdriver.Chrome(options=options, service=browser_service)
    print("finish loading driver.")
    
    yield driver
    
    print("driver closed.")
    driver.quit()
    
@pytest.fixture(scope="session")
def url():
    load_dotenv()
    BASE_URL = os.getenv("BASE_URL")
    assert BASE_URL is not None, "base url is not given."
    yield BASE_URL