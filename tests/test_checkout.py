import pytest
from pages.checkout_page import CheckoutPage
from data.test_data import ExpectedTexts, CheckoutInfo
from utils.actions import go_to_cart_with_items, do_full_checkout


class TestCheckout:

    @pytest.mark.smoke
    def test_complete_checkout(self, page):
        checkout = do_full_checkout(page)
        assert checkout.get_complete_header() == ExpectedTexts.CHECKOUT_COMPLETE_HEADER

    @pytest.mark.regression
    def test_empty_fields_error(self, page):
        cart = go_to_cart_with_items(page, count=1)
        cart.proceed_to_checkout()
        checkout = CheckoutPage(page)
        checkout.fill_info("", "", "")
        checkout.click_continue()
        assert checkout.get_error() == ExpectedTexts.CHECKOUT_ERROR_FIRST_NAME

    @pytest.mark.regression
    def test_total_price_visible(self, page):
        cart = go_to_cart_with_items(page, count=1)
        cart.proceed_to_checkout()
        checkout = CheckoutPage(page)
        info = CheckoutInfo.VALID
        checkout.fill_info(info["first_name"], info["last_name"], info["postal_code"])
        checkout.click_continue()
        total = checkout.get_total()
        assert "Total:" in total

    @pytest.mark.regression
    def test_back_home_after_checkout(self, page):
        checkout = do_full_checkout(page)
        checkout.click_back_home()
        assert "inventory" in page.url
