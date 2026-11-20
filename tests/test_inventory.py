"""
Test Suite — Inventory / Products page (4 test cases).
"""

import pytest

from data.test_data import ExpectedTexts
from utils.actions import perform_login


class TestInventory:
    """Inventory page test cases."""

    @pytest.mark.smoke
    @pytest.mark.inventory
    def test_products_are_displayed(self, page):
        """TC-04: Products page shows 6 items after login."""
        inventory = perform_login(page)
        assert inventory.get_product_count() == 6

    @pytest.mark.regression
    @pytest.mark.inventory
    def test_sort_products_name_z_to_a(self, page):
        """TC-05: Sorting Z-A reverses the default product order."""
        inventory = perform_login(page)
        inventory.sort_products("za")
        names = inventory.get_product_names()
        assert names == sorted(names, reverse=True)

    @pytest.mark.regression
    @pytest.mark.inventory
    def test_sort_products_price_low_to_high(self, page):
        """TC-06: Sorting low-to-high orders prices ascending."""
        inventory = perform_login(page)
        inventory.sort_products("lohi")
        prices = inventory.get_product_prices()
        assert prices == sorted(prices)

    @pytest.mark.smoke
    @pytest.mark.inventory
    def test_logout(self, page):
        """TC-07: User can log out and return to the login page."""
        inventory = perform_login(page)
        inventory.logout()
        assert "saucedemo.com" in page.url
        # Login button should be visible again
        assert page.is_visible("#login-button")
