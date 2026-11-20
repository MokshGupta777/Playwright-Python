"""
LoginPage — Page Object for the SauceDemo login screen.
"""

from pages.base_page import BasePage
from data.config import Config


class LoginPage(BasePage):
    """Encapsulates interactions with the login page."""

    # ── Locators ────────────────────────────────────────────────
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    # ── Actions ─────────────────────────────────────────────────

    def open(self) -> "LoginPage":
        """Navigate to the login page."""
        self.navigate(Config.BASE_URL)
        return self

    def enter_username(self, username: str) -> "LoginPage":
        self.fill(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        self.fill(self.PASSWORD_INPUT, password)
        return self

    def click_login(self) -> None:
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        """Full login flow: fill credentials and click login."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # ── Getters ─────────────────────────────────────────────────

    def get_error_message(self) -> str:
        """Return the error message displayed on failed login."""
        self.wait_for_selector(self.ERROR_MESSAGE)
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)
