import time

import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    assert driver.title == "Google"
    driver.quit()


def test_youtube():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.youtube.com/")
    assert driver.title == "YouTube"
    driver.quit()


def test_gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.gmail.com/")
    assert driver.title == "Gmail"
    driver.quit()


def test_codeproject():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.codeproject.com/")
    assert driver.title == "CodeProject - For those who code"
    driver.quit()
