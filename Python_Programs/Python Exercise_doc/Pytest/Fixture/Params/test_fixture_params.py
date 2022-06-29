import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path="D:\\Automation\\Chrome Driver\\chromedriver.exe")
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path="D:\\Automation\\mozilla\\geckodriver.exe")
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_Google(BaseTest):
    def test_google_title(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"
