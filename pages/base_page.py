"""
BasePage — parent class for all Page Objects.
Contains reusable low-level browser interaction methods.
"""

from playwright.sync_api import Page, expect


class BasePage:
    """Base class providing common page interactions."""

    def __init__(self, page: Page) -> None:
        self.page = page

    # ── Navigation ──────────────────────────────────────────────

    def navigate(self, url: str) -> None:
        """Navigate to the given URL."""
        self.page.goto(url, wait_until="domcontentloaded")

    def get_current_url(self) -> str:
        """Return the current page URL."""
        return self.page.url

    def get_title(self) -> str:
        """Return the page title."""
        return self.page.title()

    # ── Element Interactions ────────────────────────────────────

    def click(self, selector: str) -> None:
        """Click an element identified by *selector*."""
        self.page.click(selector)

    def fill(self, selector: str, text: str) -> None:
        """Clear and type *text* into the input at *selector*."""
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        """Return the inner text of the element at *selector*."""
        return self.page.inner_text(selector)

    def get_element_count(self, selector: str) -> int:
        """Return the number of elements matching *selector*."""
        return len(self.page.query_selector_all(selector))

    def is_visible(self, selector: str) -> bool:
        """Check whether the element at *selector* is visible."""
        return self.page.is_visible(selector)

    def select_option(self, selector: str, value: str) -> None:
        """Select a dropdown option by its value attribute."""
        self.page.select_option(selector, value)

    # ── Waits & Assertions ──────────────────────────────────────

    def wait_for_selector(self, selector: str, timeout: int = 10_000) -> None:
        """Wait until *selector* appears in the DOM."""
        self.page.wait_for_selector(selector, timeout=timeout)

    def expect_url_contains(self, fragment: str) -> None:
        """Assert the current URL contains *fragment*."""
        expect(self.page).to_have_url(f"*{fragment}*")

    # ── Screenshots ─────────────────────────────────────────────

    def take_screenshot(self, path: str) -> None:
        """Save a full-page screenshot to *path*."""
        self.page.screenshot(path=path, full_page=True)
