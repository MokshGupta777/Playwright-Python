from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE_BTN = "#continue"
    ERROR_MESSAGE = "[data-test='error']"
    FINISH_BTN = "#finish"
    SUMMARY_TOTAL = ".summary_total_label"
    COMPLETE_HEADER = ".complete-header"
    BACK_HOME_BTN = "#back-to-products"

    def fill_info(self, first_name, last_name, postal_code):
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.POSTAL_CODE, postal_code)

    def click_continue(self):
        self.click(self.CONTINUE_BTN)

    def get_error(self):
        self.wait_for_selector(self.ERROR_MESSAGE)
        return self.get_text(self.ERROR_MESSAGE)

    def get_total(self):
        return self.get_text(self.SUMMARY_TOTAL)

    def click_finish(self):
        self.click(self.FINISH_BTN)

    def get_complete_header(self):
        self.wait_for_selector(self.COMPLETE_HEADER)
        return self.get_text(self.COMPLETE_HEADER)

    def click_back_home(self):
        self.click(self.BACK_HOME_BTN)
