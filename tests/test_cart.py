import pytest
from pages.cart_page import CartPage
from utils.actions import do_login, add_items_to_cart, go_to_cart_with_items


class TestCart:

    @pytest.mark.smoke
    def test_add_single_product(self, page):
        inventory = do_login(page)
        inventory.add_product_to_cart(0)
        assert inventory.get_cart_badge_count() == 1

    @pytest.mark.regression
    def test_add_multiple_products(self, page):
        inventory = add_items_to_cart(page, count=3)
        assert inventory.get_cart_badge_count() == 3

    @pytest.mark.regression
    def test_remove_product(self, page):
        inventory = do_login(page)
        inventory.add_product_to_cart(0)
        inventory.remove_product(0)
        assert inventory.get_cart_badge_count() == 0

    @pytest.mark.regression
    def test_cart_has_correct_items(self, page):
        cart = go_to_cart_with_items(page, count=2)
        assert cart.get_cart_item_count() == 2

    @pytest.mark.regression
    def test_remove_item_from_cart_page(self, page):
        cart = go_to_cart_with_items(page, count=2)
        cart.remove_item(0)
        assert cart.get_cart_item_count() == 1

    @pytest.mark.regression
    def test_continue_shopping(self, page):
        cart = go_to_cart_with_items(page, count=1)
        cart.continue_shopping()
        assert "inventory" in page.url

    @pytest.mark.regression
    def test_product_name_matches_in_cart(self, page):
        inventory = do_login(page)
        inventory.wait_for_selector(inventory.ITEM_NAME)
        product_name = inventory.get_product_names()[0]
        inventory.add_product_to_cart(0)
        inventory.go_to_cart()
        cart = CartPage(page)
        assert product_name in cart.get_cart_item_names()
