import pytest
from selenium import webdriver

from Python_Exam.Selenium_Pytest.Config_data.config import TestData
from Python_Exam.Selenium_Pytest.Pages.Login_page import LoginPage

web_driver = None


@pytest.fixture(params=["chrome"], scope="class")
def driver_init(request):
    global web_driver

    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    yield
    # web_driver.close()


@pytest.fixture
def login_page_obj_fun(request):
    login_page = LoginPage(request.cls.driver)
    request.cls.login_page_obj = login_page
