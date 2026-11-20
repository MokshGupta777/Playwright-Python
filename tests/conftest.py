import pytest
from playwright.sync_api import sync_playwright
from data.config import Config


@pytest.fixture(scope="session")
def browser():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=Config.HEADLESS, slow_mo=Config.SLOW_MO)
    yield browser
    browser.close()
    pw.stop()


@pytest.fixture()
def page(browser):
    context = browser.new_context(
        viewport={"width": Config.VIEWPORT_WIDTH, "height": Config.VIEWPORT_HEIGHT}
    )
    context.set_default_timeout(Config.DEFAULT_TIMEOUT)
    context.set_default_navigation_timeout(Config.NAVIGATION_TIMEOUT)
    pg = context.new_page()
    yield pg
    pg.close()
    context.close()
