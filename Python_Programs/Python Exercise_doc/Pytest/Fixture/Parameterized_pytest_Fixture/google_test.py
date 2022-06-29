import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_init")
class BaseTest:
    pass


class TestHubSpot(BaseTest):
    @pytest.mark.parametrize("username,password",
                             [("admin@gmail.com", "admin123"), ("naveen@gmail.com", "naveen123")])
    def test_login(self, username, password):
        """
        :param username:
        :param password:
        :return:
        """
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
