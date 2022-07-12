import pytest

from Python_Exam.Selenium_Pytest.Config_data.config import TestData
from Python_Exam.Selenium_Pytest.Pages.Login_page import *
from Python_Exam.Selenium_Pytest.Tests.test_Base import BaseTest


class TestLogin(BaseTest):

    @pytest.mark.usefixtures("login_page_obj_fun")
    def test_click_on_login_button(self):
        print("This is test page")
        self.login_page_obj.do_click_on_login_button()

    @pytest.mark.usefixtures("login_page_obj_fun")
    def test_invalid_email_and_valid_password(self):
        self.login_page_obj.do_login(TestData.INVALID_USERNAME, TestData.PASSWORD)
        print("Please enter the valid USer name")
        assert "Invalid Username"

    @pytest.mark.usefixtures("login_page_obj_fun")
    def test_valid_email_and_invalid_password(self):
        self.login_page_obj.do_login(TestData.USERNAME, TestData.INVALID_PASSWORD)
        print("Please enter the valid PASSWORD")
        assert "Invalid PASSWORD"

    @pytest.mark.usefixtures("login_page_obj_fun")
    def test_invalid_email_and_invalid_password(self):
        self.login_page_obj.do_login(TestData.INVALID_USERNAME, TestData.INVALID_PASSWORD)
        print("Please enter the valid USERNAME and PASSWORD")
        assert "Invalid USERNAME and PASSWORD"
