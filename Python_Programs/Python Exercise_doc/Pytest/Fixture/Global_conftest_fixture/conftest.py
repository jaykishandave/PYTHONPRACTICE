import pytest
from selenium import webdriver

web_driver = None


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):
    global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path="D:\\Automation\\Chrome Driver\\chromedriver.exe")
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path="D:\\Automation\\mozilla\\geckodriver.exe")
    request.cls.driver = web_driver
    yield
    web_driver.close()
