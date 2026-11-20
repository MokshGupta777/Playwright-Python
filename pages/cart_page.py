"""
CartPage — Page Object for the SauceDemo shopping cart screen.
"""

from typing import List

from pages.base_page import BasePage


class CartPage(BasePage):
    """Encapsulates interactions with the cart page."""

    # ── Locators ────────────────────────────────────────────────
    CART_ITEM = ".cart_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    ITEM_QUANTITY = ".cart_quantity"
    REMOVE_BTN = "button[data-test^='remove']"
    CONTINUE_SHOPPING_BTN = "#continue-shopping"
    CHECKOUT_BTN = "#checkout"

    # ── Actions ─────────────────────────────────────────────────

    def get_cart_item_count(self) -> int:
        return self.get_element_count(self.CART_ITEM)

    def get_cart_item_names(self) -> List[str]:
        elements = self.page.query_selector_all(self.ITEM_NAME)
        return [el.inner_text() for el in elements]

    def remove_item_by_index(self, index: int = 0) -> None:
        buttons = self.page.query_selector_all(self.REMOVE_BTN)
        if index < len(buttons):
            buttons[index].click()

    def proceed_to_checkout(self) -> None:
        self.click(self.CHECKOUT_BTN)

    def continue_shopping(self) -> None:
        self.click(self.CONTINUE_SHOPPING_BTN)
