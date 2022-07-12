from selenium.webdriver.common.by import By

from Python_Exam.Selenium_Pytest.Config_data.config import TestData
from Python_Exam.Selenium_Pytest.Pages.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL = (By.XPATH, "//*[@name='email']")
    PASSWORD = (By.XPATH, "//*[@id='loginModal']/div/div/div/form/div[2]/input")
    LOGIN_BUTTON_HOME = (By.XPATH,"((//*[@id='loginButton'])[2])")
    SIGNIN_BUTTON = (By.XPATH,"//*[@id='login-submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.SIGNIN_BUTTON)

    def do_click_on_login_button(self):
        self.do_click(self.LOGIN_BUTTON_HOME)
