Playwright Python Test Automation

A professional-grade **end-to-end test automation framework** built with **Playwright (Sync API)** and **Python**, following the **Page Object Model (POM)** design pattern.

> **Target Application:** [SauceDemo](https://www.saucedemo.com/)

---

## 📁 Project Structure

```
Playwright PY/
├── .github/workflows/       # CI/CD pipeline (GitHub Actions)
│   └── tests.yml
├── data/                    # Test data & configuration
│   ├── config.py
│   └── test_data.py
├── pages/                   # Page Object Model classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/                   # Test cases (pytest)
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── utils/                   # Reusable utilities & actions
│   ├── actions.py
│   └── helpers.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## 🚀 Setup

```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install Playwright browsers
playwright install chromium

# 4. Run all tests
pytest

# 5. Run by marker
pytest -m smoke
pytest -m regression
```

## 📊 Reports

HTML test report is generated at `report.html` after each run.

## ⚙️ CI/CD

Tests run automatically on every **push** and **pull request** via GitHub Actions. See `.github/workflows/tests.yml`.

---

**Author:** Moksh G  
**License:** MIT
