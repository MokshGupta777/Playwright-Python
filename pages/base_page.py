from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url, wait_until="domcontentloaded")

    def get_current_url(self):
        return self.page.url

    def get_title(self):
        return self.page.title()

    def click(self, selector):
        self.page.click(selector)

    def fill(self, selector, text):
        self.page.fill(selector, text)

    def get_text(self, selector):
        return self.page.inner_text(selector)

    def get_element_count(self, selector):
        return len(self.page.query_selector_all(selector))

    def is_visible(self, selector):
        return self.page.is_visible(selector)

    def select_option(self, selector, value):
        self.page.select_option(selector, value)

    def wait_for_selector(self, selector, timeout=10_000):
        self.page.wait_for_selector(selector, timeout=timeout)
