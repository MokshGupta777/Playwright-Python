"""
Configuration settings for the test automation framework.
"""


class Config:
    """Global configuration for the test suite."""

    # Application Under Test
    BASE_URL = "https://www.saucedemo.com"

    # Browser Settings
    BROWSER = "chromium"
    HEADLESS = True
    SLOW_MO = 0  # milliseconds between actions (useful for debugging)
    VIEWPORT_WIDTH = 1280
    VIEWPORT_HEIGHT = 720

    # Timeouts (in milliseconds)
    DEFAULT_TIMEOUT = 30_000
    NAVIGATION_TIMEOUT = 60_000

    # Screenshot & Trace
    SCREENSHOT_ON_FAILURE = True
    TRACE_ON = False
