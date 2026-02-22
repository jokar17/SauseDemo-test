# SauceDemo Test Automation

Automated end-to-end test suite for [SauceDemo](https://www.saucedemo.com), 
built with Python, Selenium, and pytest following the Page Object Model pattern.

## Tech Stack

- Python 
- Selenium 
- pytest
- pytest-html

## Project Structure
```
SauseDemoTest/
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── information_page.py
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_information.py
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## Installation

1. Clone the repository
```bash
   git clone https://github.com/jokar17/SauseDemo-test.git
   cd SauseDemo-test
```

2. Create and activate a virtual environment
```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

## Running Tests

Run all tests with Chrome (default):
```bash
pytest
```

Run with a specific browser:
```bash
pytest --browser=chrome
pytest --browser=firefox
```

An HTML report will be automatically generated at `reports/report.html`.  
Failed tests will include a screenshot attached to the report.

## Test Coverage

| Module | Test Cases |
|---|---|
| Login | Valid login, error messages, empty fields |
| Inventory | Sorting (A-Z, Z-A, price), add to cart |
| Cart | Item count, remove item, navigation |
| Checkout | Form validation, missing fields, navigation |

## Design Pattern

This project follows the **Page Object Model (POM)** pattern, separating page 
interactions from test logic to improve maintainability and readability.
