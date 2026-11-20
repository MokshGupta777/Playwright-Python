class Users:
    STANDARD = {"username": "standard_user", "password": "secret_sauce"}
    LOCKED_OUT = {"username": "locked_out_user", "password": "secret_sauce"}
    INVALID = {"username": "invalid_user", "password": "wrong_password"}


class CheckoutInfo:
    VALID = {"first_name": "Moksh", "last_name": "Gupta", "postal_code": "110001"}
    EMPTY = {"first_name": "", "last_name": "", "postal_code": ""}


class ExpectedTexts:
    LOGIN_ERROR_INVALID = "Epic sadface: Username and password do not match any user in this service"
    LOGIN_ERROR_LOCKED = "Epic sadface: Sorry, this user has been locked out."
    LOGIN_ERROR_EMPTY_USERNAME = "Epic sadface: Username is required"
    CHECKOUT_ERROR_FIRST_NAME = "Error: First Name is required"
    CHECKOUT_COMPLETE_HEADER = "Thank you for your order!"
    INVENTORY_TITLE = "Products"
