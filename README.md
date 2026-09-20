# QualityForgeAI

QualityForgeAI is a Selenium UI automation portfolio project built with Python, Pytest, and Page Object Model.

## Project Structure

```text
qualityforge-ai/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_checkout.py
├── utilities/
│   └── __init__.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Run Tests

```bash
python -m pytest
```

Run smoke tests:

```bash
python -m pytest -m smoke
```

Run regression tests:

```bash
python -m pytest -m regression
```
