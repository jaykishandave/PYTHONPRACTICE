import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None


@pytest.fixture()
def setup_module():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.google.com/")


@pytest.mark.usefixtures(setup_module)
def teardown_module():
    driver.quit()


@pytest.mark.usefixtures(setup_module)
def test_google_title():
    assert driver.title == "Google"


@pytest.mark.usefixtures(setup_module)
def test_google_url():
    assert driver.current_url == "https://www.google.com/"
