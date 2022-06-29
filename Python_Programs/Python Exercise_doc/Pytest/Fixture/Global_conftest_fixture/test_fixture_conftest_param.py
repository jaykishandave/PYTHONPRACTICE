import pytest


@pytest.mark.usefixtures("driver_init")
class BaseTest:
    pass


class Test_Google(BaseTest):
    def test_google_title(self):
        # self.web_driver.get("https://www.google.com/")
        self.driver.get("https://www.google.com/")
        # assert self.web_driver.title == "Google"
        assert self.driver.title == "Google"

    # def test_google_url(self):
    # self.web_driver.get("https://www.google.com/")
    #     assert self.web_driver.current_url == "https://www.google.com/"
