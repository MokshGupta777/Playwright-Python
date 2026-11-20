"""
InventoryPage — Page Object for the SauceDemo products/inventory screen.
"""

from typing import List

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Encapsulates interactions with the inventory (products) page."""

    # ── Locators ────────────────────────────────────────────────
    TITLE = ".title"
    INVENTORY_ITEM = ".inventory_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    ADD_TO_CART_BTN = "[data-test^='add-to-cart']"
    REMOVE_BTN = "button[data-test^='remove']"
    SORT_DROPDOWN = "[data-test='product-sort-container']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    BURGER_MENU = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    # ── Actions ─────────────────────────────────────────────────

    def get_page_title(self) -> str:
        return self.get_text(self.TITLE)

    def get_product_count(self) -> int:
        return self.get_element_count(self.INVENTORY_ITEM)

    def get_product_names(self) -> List[str]:
        elements = self.page.query_selector_all(self.ITEM_NAME)
        return [el.inner_text() for el in elements]

    def get_product_prices(self) -> List[float]:
        elements = self.page.query_selector_all(self.ITEM_PRICE)
        return [float(el.inner_text().replace("$", "")) for el in elements]

    def add_product_to_cart_by_index(self, index: int = 0) -> None:
        buttons = self.page.locator(self.ADD_TO_CART_BTN)
        buttons.nth(index).click()
        # Wait for the UI to update after adding
        self.page.wait_for_timeout(300)

    def remove_product_by_index(self, index: int = 0) -> None:
        buttons = self.page.query_selector_all(self.REMOVE_BTN)
        if index < len(buttons):
            buttons[index].click()

    def get_cart_badge_count(self) -> int:
        if self.is_visible(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def go_to_cart(self) -> None:
        self.click(self.CART_LINK)

    def sort_products(self, value: str) -> None:
        """Sort products. Values: az, za, lohi, hilo"""
        self.select_option(self.SORT_DROPDOWN, value)

    def click_product_by_name(self, name: str) -> None:
        self.page.click(f"text={name}")

    def logout(self) -> None:
        self.click(self.BURGER_MENU)
        self.page.wait_for_selector(self.LOGOUT_LINK, state="visible")
        self.click(self.LOGOUT_LINK)
