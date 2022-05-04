import time

from Python_Selenium.Fixture.Pytest_Fixture import *


class TestValidationForInfo:
    @pytest.mark.usefixtures("setup_browser", "get_location_url")
    def test_validation(self, get_location_url):
        get_url = get_location_url
        assert "seleniumeasy" in get_url, "Google is missing from the url"
        assert "https://demo.seleniumeasy.com/" == get_url, "Google is missing from the url"

    @pytest.mark.usefixtures("click_no_thanks")
    def test_validate_learn_dialog(self, click_no_thanks):
        time.sleep(10)
        thanks = click_no_thanks
        thanks.click()



