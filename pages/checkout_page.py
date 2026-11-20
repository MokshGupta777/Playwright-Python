"""
CheckoutPage — Page Object for the SauceDemo checkout screens
(step-one, step-two, and complete).
"""

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Encapsulates interactions across all checkout steps."""

    # ── Locators — Step One (Info) ──────────────────────────────
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BTN = "#continue"
    CANCEL_BTN = "#cancel"
    ERROR_MESSAGE = "[data-test='error']"

    # ── Locators — Step Two (Overview) ──────────────────────────
    FINISH_BTN = "#finish"
    SUMMARY_TOTAL = ".summary_total_label"

    # ── Locators — Complete ─────────────────────────────────────
    COMPLETE_HEADER = ".complete-header"
    BACK_HOME_BTN = "#back-to-products"

    # ── Actions — Step One ──────────────────────────────────────

    def fill_checkout_info(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.fill(self.LAST_NAME_INPUT, last_name)
        self.fill(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self) -> None:
        self.click(self.CONTINUE_BTN)

    def get_checkout_error(self) -> str:
        self.wait_for_selector(self.ERROR_MESSAGE)
        return self.get_text(self.ERROR_MESSAGE)

    # ── Actions — Step Two ──────────────────────────────────────

    def get_total(self) -> str:
        return self.get_text(self.SUMMARY_TOTAL)

    def click_finish(self) -> None:
        self.click(self.FINISH_BTN)

    # ── Actions — Complete ──────────────────────────────────────

    def get_complete_header(self) -> str:
        self.wait_for_selector(self.COMPLETE_HEADER)
        return self.get_text(self.COMPLETE_HEADER)

    def click_back_home(self) -> None:
        self.click(self.BACK_HOME_BTN)
