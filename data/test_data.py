"""
Centralized test data for all test suites.
"""


class Users:
    """Login credentials for SauceDemo."""

    STANDARD = {"username": "standard_user", "password": "secret_sauce"}
    LOCKED_OUT = {"username": "locked_out_user", "password": "secret_sauce"}
    INVALID = {"username": "invalid_user", "password": "wrong_password"}


class CheckoutInfo:
    """Checkout form data."""

    VALID = {
        "first_name": "Moksh",
        "last_name": "Gupta",
        "postal_code": "110001",
    }
    EMPTY = {
        "first_name": "",
        "last_name": "",
        "postal_code": "",
    }


class ExpectedTexts:
    """Expected UI strings for assertions."""

    LOGIN_ERROR_INVALID = (
        "Epic sadface: Username and password do not match any user in this service"
    )
    LOGIN_ERROR_LOCKED = "Epic sadface: Sorry, this user has been locked out."
    CHECKOUT_ERROR_FIRST_NAME = "Error: First Name is required"
    CHECKOUT_COMPLETE_HEADER = "Thank you for your order!"
    INVENTORY_TITLE = "Products"
