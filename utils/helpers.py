"""
General-purpose utility functions used across test suites.
"""

import os
from datetime import datetime


def get_timestamp() -> str:
    """Return a filesystem-safe timestamp string."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def ensure_dir(path: str) -> str:
    """Create the directory at *path* if it does not exist and return *path*."""
    os.makedirs(path, exist_ok=True)
    return path


def screenshot_path(test_name: str) -> str:
    """Generate a unique screenshot path under the screenshots/ directory."""
    folder = ensure_dir("screenshots")
    return os.path.join(folder, f"{test_name}_{get_timestamp()}.png")
