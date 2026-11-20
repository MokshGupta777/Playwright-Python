"""
Reusable action helpers that orchestrate multi-step flows
across page objects, keeping tests clean and DRY.
"""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from data.test_data import Users, CheckoutInfo


def perform_login(page, user: dict | None = None) -> InventoryPage:
    """Login with the given user (defaults to STANDARD) and return InventoryPage."""
    if user is None:
        user = Users.STANDARD
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(user["username"], user["password"])
    return InventoryPage(page)


def add_items_and_go_to_cart(page, count: int = 1) -> CartPage:
    """Login → add *count* items → navigate to cart → return CartPage."""
    inventory = perform_login(page)
    for i in range(count):
        inventory.add_product_to_cart_by_index(i)
    inventory.go_to_cart()
    return CartPage(page)


def complete_checkout_flow(page) -> str:
    """Login → add item → cart → checkout → finish. Returns the confirmation header."""
    cart = add_items_and_go_to_cart(page, count=1)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(page)
    info = CheckoutInfo.VALID
    checkout.fill_checkout_info(info["first_name"], info["last_name"], info["postal_code"])
    checkout.click_continue()
    checkout.click_finish()

    return checkout.get_complete_header()
