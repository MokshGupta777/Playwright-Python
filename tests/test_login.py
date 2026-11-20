"""
Test Suite — Login functionality (3 test cases).
"""

import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from data.test_data import Users, ExpectedTexts


class TestLogin:
    """Login page test cases."""

    @pytest.mark.smoke
    @pytest.mark.login
    def test_valid_login(self, page):
        """TC-01: Standard user can log in successfully."""
        login = LoginPage(page)
        login.open()
        login.login(Users.STANDARD["username"], Users.STANDARD["password"])

        inventory = InventoryPage(page)
        assert inventory.get_page_title() == ExpectedTexts.INVENTORY_TITLE

    @pytest.mark.regression
    @pytest.mark.login
    def test_invalid_login(self, page):
        """TC-02: Invalid credentials show an error message."""
        login = LoginPage(page)
        login.open()
        login.login(Users.INVALID["username"], Users.INVALID["password"])

        assert login.get_error_message() == ExpectedTexts.LOGIN_ERROR_INVALID

    @pytest.mark.regression
    @pytest.mark.login
    def test_locked_out_user(self, page):
        """TC-03: Locked-out user sees a locked-out error message."""
        login = LoginPage(page)
        login.open()
        login.login(Users.LOCKED_OUT["username"], Users.LOCKED_OUT["password"])

        assert login.get_error_message() == ExpectedTexts.LOGIN_ERROR_LOCKED
