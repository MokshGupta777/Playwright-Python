from pages.base_page import BasePage


class InventoryPage(BasePage):

    TITLE = ".title"
    INVENTORY_ITEM = ".inventory_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    ADD_TO_CART_BTN = "[data-test^='add-to-cart']"
    REMOVE_BTN = "[data-test^='remove']"
    SORT_DROPDOWN = "[data-test='product-sort-container']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    BURGER_MENU = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"
    DETAIL_NAME = "[data-test='inventory-item-name']"
    BACK_BUTTON = "#back-to-products"

    def get_page_title(self):
        return self.get_text(self.TITLE)

    def get_product_count(self):
        return self.get_element_count(self.INVENTORY_ITEM)

    def get_product_names(self):
        elements = self.page.query_selector_all(self.ITEM_NAME)
        return [el.inner_text() for el in elements]

    def get_product_prices(self):
        elements = self.page.query_selector_all(self.ITEM_PRICE)
        return [float(el.inner_text().replace("$", "")) for el in elements]

    def add_product_to_cart(self, index=0):
        self.page.locator(self.ADD_TO_CART_BTN).nth(index).click()
        self.page.wait_for_timeout(300)

    def remove_product(self, index=0):
        self.page.locator(self.REMOVE_BTN).nth(index).click()

    def get_cart_badge_count(self):
        if self.is_visible(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def sort_products(self, value):
        self.select_option(self.SORT_DROPDOWN, value)

    def click_product(self, name):
        self.page.click(f"text={name}")

    def get_detail_product_name(self):
        return self.get_text(self.DETAIL_NAME)

    def go_back_to_products(self):
        self.click(self.BACK_BUTTON)

    def logout(self):
        self.click(self.BURGER_MENU)
        self.page.wait_for_selector(self.LOGOUT_LINK, state="visible")
        self.click(self.LOGOUT_LINK)
