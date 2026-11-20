import pytest
from data.test_data import ExpectedTexts
from utils.actions import do_login


class TestInventory:

    @pytest.mark.smoke
    def test_products_page_title(self, page):
        inventory = do_login(page)
        assert inventory.get_page_title() == ExpectedTexts.INVENTORY_TITLE

    @pytest.mark.smoke
    def test_six_products_displayed(self, page):
        inventory = do_login(page)
        assert inventory.get_product_count() == 6

    @pytest.mark.regression
    def test_sort_z_to_a(self, page):
        inventory = do_login(page)
        inventory.sort_products("za")
        names = inventory.get_product_names()
        assert names == sorted(names, reverse=True)

    @pytest.mark.regression
    def test_sort_price_low_to_high(self, page):
        inventory = do_login(page)
        inventory.sort_products("lohi")
        prices = inventory.get_product_prices()
        assert prices == sorted(prices)

    @pytest.mark.regression
    def test_sort_price_high_to_low(self, page):
        inventory = do_login(page)
        inventory.sort_products("hilo")
        prices = inventory.get_product_prices()
        assert prices == sorted(prices, reverse=True)

    @pytest.mark.regression
    def test_product_detail_page(self, page):
        inventory = do_login(page)
        first_product = inventory.get_product_names()[0]
        inventory.click_product(first_product)
        assert inventory.get_detail_product_name() == first_product

    @pytest.mark.regression
    def test_back_from_product_detail(self, page):
        inventory = do_login(page)
        inventory.click_product(inventory.get_product_names()[0])
        inventory.go_back_to_products()
        assert inventory.get_product_count() == 6

    @pytest.mark.smoke
    def test_logout(self, page):
        inventory = do_login(page)
        inventory.logout()
        assert page.is_visible("#login-button")
