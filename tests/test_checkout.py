"""
Test Suite — Checkout flow (2 test cases).
"""

import pytest

from pages.checkout_page import CheckoutPage
from data.test_data import ExpectedTexts, CheckoutInfo
from utils.actions import add_items_and_go_to_cart, complete_checkout_flow


class TestCheckout:
    """Checkout flow test cases."""

    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_complete_checkout(self, page):
        """TC-11: Full checkout flow completes with a confirmation message."""
        header = complete_checkout_flow(page)
        assert header == ExpectedTexts.CHECKOUT_COMPLETE_HEADER

    @pytest.mark.regression
    @pytest.mark.checkout
    def test_checkout_empty_fields_shows_error(self, page):
        """TC-12: Submitting checkout without info shows a validation error."""
        cart = add_items_and_go_to_cart(page, count=1)
        cart.proceed_to_checkout()

        checkout = CheckoutPage(page)
        checkout.fill_checkout_info(
            CheckoutInfo.EMPTY["first_name"],
            CheckoutInfo.EMPTY["last_name"],
            CheckoutInfo.EMPTY["postal_code"],
        )
        checkout.click_continue()

        assert checkout.get_checkout_error() == ExpectedTexts.CHECKOUT_ERROR_FIRST_NAME
