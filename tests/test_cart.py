"""
Test Suite — Shopping Cart (3 test cases).
"""

import pytest

from utils.actions import perform_login, add_items_and_go_to_cart


class TestCart:
    """Cart page test cases."""

    @pytest.mark.smoke
    @pytest.mark.cart
    def test_add_product_to_cart(self, page):
        """TC-08: Adding a product updates the cart badge to 1."""
        inventory = perform_login(page)
        inventory.add_product_to_cart_by_index(0)
        assert inventory.get_cart_badge_count() == 1

    @pytest.mark.regression
    @pytest.mark.cart
    def test_remove_product_from_cart(self, page):
        """TC-09: Removing the only product makes the badge disappear."""
        inventory = perform_login(page)
        inventory.add_product_to_cart_by_index(0)
        inventory.remove_product_by_index(0)
        assert inventory.get_cart_badge_count() == 0

    @pytest.mark.regression
    @pytest.mark.cart
    def test_cart_shows_added_items(self, page):
        """TC-10: Cart page lists exactly the items that were added."""
        cart = add_items_and_go_to_cart(page, count=2)
        assert cart.get_cart_item_count() == 2
