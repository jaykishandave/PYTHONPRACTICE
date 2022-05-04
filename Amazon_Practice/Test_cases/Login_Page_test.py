from Amazon_Practice.Page_Object.Login_page_object import *


class TestValidation:

    @pytest.mark.parametrize("setup_browser",
                             [{"Browser": 'chrome', "url": con.url}, {"Browser": 'firefox', "url": con.url}],
                             indirect=True)
    def test_validation(self, setup_browser):
        get_url = get_location_url()
        print("Available url is" + get_url)
        assert "seleniumeasy" in get_url, "seleniumeasy is missing from the url"
        # assert "google" == get_url, "Google is missing from the url"

    def test_learn_selenium_dialog(self):
        no = learn_selenium_dialog()
        no.click()


    # def test_enter_email_or_mobile_phone_number(self):
    #     time.sleep(10)
    #     email = locator_email_or_mobile_phone_number()
    #     email.send_keys("demo@gmail.com")
