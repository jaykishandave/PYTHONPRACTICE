import time

import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("D:\Automation\Chrome Driver\chromedriver.exe")


@pytest.fixture()
def setup_browser():
    time.sleep(5)
    driver.get("https://demo.seleniumeasy.com/")
    yield
    # driver.close()


@pytest.fixture()
def get_location_url():
    url = driver.current_url
    yield url

@pytest.fixture()
def click_no_thanks():
    thanks = driver.find_element(By.XPATH,"//div[@id='at-cv-lightbox-button-holder']//a[@class='at-cv-button at-cv-lightbox-yesno at-cm-no-button']")
    yield thanks


