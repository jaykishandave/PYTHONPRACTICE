import time
import pytest
from Amazon_Practice.Config.Config import Configuration

con = Configuration


@pytest.fixture()
def setup_browser(request):
    time.sleep(5)
    params = getattr(request, "param")
    print(params)
    web_driver = None
    if params["Browser"] == "chrome":
        web_driver = con.driver_chrome
    if params["Browser"] == "firefox":
        web_driver = con.driver_firefox
    web_driver.get(params["url"])
    yield
# ==============================
# @pytest.fixture()
# def setup_browser():
#     time.sleep(5)
#     con.driver_chrome.get(con.url)
#     yield
#     # driver.close()
