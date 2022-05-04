from selenium import webdriver
import pytest


class Configuration:
    driver_chrome = webdriver.Chrome(executable_path="D:\\Automation\\Chrome Driver\\chromedriver.exe")
    driver_firefox = webdriver.Firefox(executable_path="D:\\Automation\\mozilla\\geckodriver.exe")
    url = "https://demo.seleniumeasy.com/"
