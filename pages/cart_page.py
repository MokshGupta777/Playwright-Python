from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ITEM = ".cart_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    REMOVE_BTN = "[data-test^='remove']"
    CONTINUE_SHOPPING_BTN = "#continue-shopping"
    CHECKOUT_BTN = "#checkout"

    def get_cart_item_count(self):
        return self.get_element_count(self.CART_ITEM)

    def get_cart_item_names(self):
        elements = self.page.query_selector_all(self.ITEM_NAME)
        return [el.inner_text() for el in elements]

    def remove_item(self, index=0):
        self.page.locator(self.REMOVE_BTN).nth(index).click()

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)
