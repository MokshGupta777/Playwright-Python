import os
from datetime import datetime


def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def screenshot_path(test_name):
    os.makedirs("screenshots", exist_ok=True)
    return f"screenshots/{test_name}_{get_timestamp()}.png"
