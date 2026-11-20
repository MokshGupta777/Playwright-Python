import pytest
from pages.login_page import LoginPage
from data.test_data import Users, ExpectedTexts


class TestLogin:

    @pytest.mark.smoke
    def test_valid_login(self, page):
        login = LoginPage(page)
        login.open()
        login.login(Users.STANDARD["username"], Users.STANDARD["password"])
        assert "inventory" in page.url

    @pytest.mark.regression
    def test_invalid_credentials(self, page):
        login = LoginPage(page)
        login.open()
        login.login(Users.INVALID["username"], Users.INVALID["password"])
        assert login.get_error_message() == ExpectedTexts.LOGIN_ERROR_INVALID

    @pytest.mark.regression
    def test_locked_out_user(self, page):
        login = LoginPage(page)
        login.open()
        login.login(Users.LOCKED_OUT["username"], Users.LOCKED_OUT["password"])
        assert login.get_error_message() == ExpectedTexts.LOGIN_ERROR_LOCKED

    @pytest.mark.regression
    def test_empty_credentials(self, page):
        login = LoginPage(page)
        login.open()
        login.login("", "")
        assert login.get_error_message() == ExpectedTexts.LOGIN_ERROR_EMPTY_USERNAME

    @pytest.mark.smoke
    def test_login_page_title(self, page):
        login = LoginPage(page)
        login.open()
        assert "Swag Labs" in page.title()
