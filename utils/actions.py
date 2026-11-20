from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from data.test_data import Users, CheckoutInfo


def do_login(page, user=None):
    if user is None:
        user = Users.STANDARD
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(user["username"], user["password"])
    return InventoryPage(page)


def add_items_to_cart(page, count=1):
    inventory = do_login(page)
    for i in range(count):
        inventory.add_product_to_cart(i)
    return inventory


def go_to_cart_with_items(page, count=1):
    inventory = add_items_to_cart(page, count)
    inventory.go_to_cart()
    return CartPage(page)


def do_full_checkout(page):
    cart = go_to_cart_with_items(page, count=1)
    cart.proceed_to_checkout()
    checkout = CheckoutPage(page)
    info = CheckoutInfo.VALID
    checkout.fill_info(info["first_name"], info["last_name"], info["postal_code"])
    checkout.click_continue()
    checkout.click_finish()
    return checkout
