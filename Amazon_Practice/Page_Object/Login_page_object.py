from Amazon_Practice.conftest import *
from selenium.webdriver.common.by import By


class Amazon_POM:
    # Learn selenium to automate with Seleniumeasy.com dialogbox
    no_thanks = "//div[@id='at-cv-lightbox-button-holder']//a[text()='No, thanks!']"


# Learn selenium to automate with Seleniumeasy.com dialogbox
def learn_selenium_dialog():
    no_thanks = None
    no_thanks = con.driver_chrome.find_element(By.ID, Amazon_POM.no_thanks)
    if params["Browser"] == "firefox":
        no_thanks = con.driver_firefox.find_element(By.ID, Amazon_POM.no_thanks)

    return no_thanks


def get_location_url():
    url = con.driver_chrome.current_url
    return url
