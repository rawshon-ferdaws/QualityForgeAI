Project Architecture / Current Framework Summary

| Area                   | What I am Applying                                                                                                                                                                                  |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purpose of Testing** | To verify that the application works correctly across **UI, API, and backend layers**, catch defects early, validate critical user workflows, and ensure reliable releases through automated testing. |
| **What I Am Doing**    | Automating **positive, negative, regression, integration, and E2E scenarios** using reusable framework components.                                                                                    |
| **Selenium**           | UI automation using **Page Object Model (POM)**, locators, explicit waits, reusable actions, and browser automation.                                                                                  |
| **Browser**            | **Firefox — current stable execution browser.** Chrome is supported but currently has a Chrome/WebDriver stability issue in my environment.                                                           |
| **Pytest**             | Test execution, fixtures, assertions, markers, test organization, setup and teardown.                                                                                                                 |
| **API**                | API automation using **Python Requests** — GET, POST, PUT/PATCH, DELETE, payloads, parameters, headers, and response validation.                                                                      |
| **Database**           | **SQL-based** backend/data validation.                                                                                                                                                                |
| **CI/CD Pipeline**     | **GitHub Actions** for automated test execution on code changes.                                                                                                                                      |
| **Docker**             | Reproducible and consistent test execution environment.                                                                                                                                               |
| **AI Pipeline**        | LLM-assisted **failure analysis, test generation, test-data generation, and CI test summaries**.                                                                                                      |
| **LLM**                | **Yes** — existing LLM integration for AI-assisted QA.                                                                                                                                                |
| **LLM Trainer**        | **No** — I am not training an LLM from scratch.                                                                                                                                                       |
| **Current Status**     | **UI automation complete — 18/18 tests passing** across Login, Products, Cart, Checkout, and E2E purchase flow.                                                                                       |

UI Testing — Selenium + POM Automation

| Point                  | What I Applied                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Purpose**            | Verify critical user workflows through the browser, detect functional defects, and provide confidence before release.          |
| **Framework**          | **Python + Selenium WebDriver + Pytest + Page Object Model (POM)** automation framework.                                       |
| **Application Tested** | **SauceDemo** web application.                                                                                                 |
| **Browser**            | **Firefox** as the current stable execution browser; framework also supports Chrome.                                           |
| **POM**                | Separate Page Objects for **Login, Products, Cart, and Checkout**.                                                             |
| **Base Page**          | Reusable Selenium actions such as **click, type, get text, visibility/presence checks, and explicit waits**.                   |
| **Locators**           | **ID, CSS Selector, and Class Name** locators centralized inside Page Objects.                                                 |
| **Pytest**             | **Fixtures, assertions, test organization, setup/teardown**, and reusable WebDriver configuration.                             |
| **Test Data**          | Test/user data externalized in **JSON**.                                                                                       |
| **Configuration**      | Browser, base URL, and timeout values managed through **`config.ini`**.                                                        |
| **Functional Testing** | Verified application functions such as **login, product selection, cart operations, checkout, and purchase completion**.       |
| **Positive Testing**   | Valid login, adding/removing products, valid checkout information, and successful purchase.                                    |
| **Negative Testing**   | Invalid login, locked-out user, and missing checkout-field validations.                                                        |
| **Smoke Testing**      | Critical functionality such as **login and core purchase flow** can be selected as the fast build-validation suite.            |
| **Sanity Testing**     | Focused tests can validate a specific changed/fixed area, such as **Cart or Checkout**, before broader regression.             |
| **Regression Testing** | The complete automated UI suite can be rerun to verify existing functionality after application changes.                       |
| **Risk-Based Testing** | Prioritized business-critical flows such as **Login → Product → Cart → Checkout → Order Confirmation**.                        |
| **Shift-Left Testing** | Automated tests are structured to run early through **Pytest and later CI/CD**, helping detect defects earlier in development. |
| **E2E Testing**        | Complete **Login → Products → Cart → Checkout → Order Confirmation** workflow.                                                 |
| **Contract Testing**   | Applied in the **API layer**, including response structure and **JSON Schema** validation—not Selenium UI testing.             |
| **UI Result**          | **18/18 UI tests passing**.                                                                                                    |

UI Page Object Layer

| Page               | Main Responsibility                                                   | Status |
| ------------------ | --------------------------------------------------------------------- | ------ |
| `base_page.py`     | Reusable actions, explicit waits, click/type/text/visibility/presence | ✅      |
| `login_page.py`    | Username, password, login, error handling                             | ✅      |
| `products_page.py` | Products, add/remove cart, cart badge, navigation                     | ✅      |
| `cart_page.py`     | Cart items, price, remove item, checkout navigation                   | ✅      |
| `checkout_page.py` | Customer info, validation errors, overview, finish, confirmation      | ✅      |

Tests — Current Shape

| Test File                        | What It Covers                                                              | Status    |
| -------------------------------- | --------------------------------------------------------------------------- | --------- |
| `tests/ui/test_login.py`         | Valid login, invalid login, locked-out user                                 | ✅ Good    |
| `tests/ui/test_products.py`      | Products page, add product, remove product                                  | ✅ Good    |
| `tests/ui/test_cart.py`          | Cart display, item validation, price, removal                               | ✅ Good    |
| `tests/ui/test_checkout.py`      | Checkout page, valid data, required-field negatives, overview, completion   | ✅ Good    |
| `tests/ui/test_e2e_purchase.py`  | Complete Login → Product → Cart → Checkout → Confirmation flow              | ✅ Good    |
| `tests/api/test_api.py`          | GET, POST, PUT, PATCH, DELETE, parameters, 404s, response/schema validation | ✅ Good    |
| `tests/api/test_negative_api.py` | Additional negative API scenario                                            | ✅ Passing |
| `tests/api/test_orders_api.py`   | Order-response validation example                                           | ✅ Passing |
| `tests/api/test_products_api.py` | Product-response validation example                                         | ✅ Passing |
| `tests/api/test_users.py`        | User GET, collection, query-parameter scenarios                             | ✅ Passing |

API Testing — Python Requests + Pytest

| Point                        | What I Applied                                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Purpose**                  | Verify backend APIs return the expected **status codes, headers, response data, structure, and data types** independently of the UI. |
| **Framework**                | **Python + Requests + Pytest** API automation framework.                                                                             |
| **API Used**                 | **JSONPlaceholder REST API** for API automation practice.                                                                            |
| **API Client**               | Reusable `APIClient` methods for **GET, POST, PUT, PATCH, and DELETE** requests.                                                     |
| **Endpoints**                | Centralized API endpoints in `endpoints.py`, avoiding repeated hardcoded endpoints in tests.                                         |
| **Configuration**            | API base URL and timeout managed through **`config.ini`**.                                                                           |
| **Test Data**                | Request payloads externalized into **`api_payloads.json`**.                                                                          |
| **GET Testing**              | Tested **single resources, collections, and query-parameter filtering**.                                                             |
| **POST Testing**             | Sent creation requests and validated the returned response.                                                                          |
| **PUT Testing**              | Tested complete resource-update requests.                                                                                            |
| **PATCH Testing**            | Tested partial resource updates.                                                                                                     |
| **DELETE Testing**           | Tested delete requests and expected response status.                                                                                 |
| **Query Parameters**         | Tested resource filtering using parameters such as **`userId`**.                                                                     |
| **Status Code Validation**   | Validated expected status codes including **200, 201, and 404**.                                                                     |
| **Header Validation**        | Verified response **Content-Type** is JSON.                                                                                          |
| **Response Body Validation** | Validated response **keys, values, and data types**.                                                                                 |
| **Reusable Validators**      | Created reusable validation methods in **`validators.py`**.                                                                          |
| **Positive Testing**         | Tested valid GET/POST/PUT/PATCH/DELETE requests and expected responses.                                                              |
| **Negative Testing**         | Tested **nonexistent users/posts** and validated **404** responses.                                                                  |
| **Functional Testing**       | Verified individual REST operations behave according to expected API behavior.                                                       |
| **Contract Testing**         | Validated the API response contract using **JSON Schema**.                                                                           |
| **Schema Validation**        | Validated required fields such as `id`, `name`, `username`, `email`, `address`, etc., and expected data types.                       |
| **Regression Testing**       | API suite can be rerun to detect changes or regressions in existing API behavior.                                                    |
| **Smoke Testing**            | Critical API checks can be selected for fast API health/build validation.                                                            |
| **Risk-Based Testing**       | Prioritized important API behavior including successful operations, response integrity, error handling, and API contracts.           |
| **Shift-Left Testing**       | API tests run independently of the UI and are structured for **CI/CD execution**, enabling earlier defect detection.                 |
| **API Result**               | **17/17 API tests passing** in the combined project run.                                                                             |

AI-assisted testing / LLM integration

I integrated an OpenAI GPT model through an API into my Python QA automation framework. I designed QA-specific prompts and built reusable AI components for test failure analysis, requirement-based test scenario generation, test-data generation, and CI test-result summarization. I integrated these capabilities with Pytest and validated the AI layer through dedicated integration tests, with all 5 tests passing.

| Area                        | What I Implemented                                                                                                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purpose**                 | I added an AI-assisted testing layer to enhance test design, failure analysis, test-data generation, and CI test-result analysis.                       |
| **LLM Integration**         | I integrated an **OpenAI GPT model through the API** into my Python QA automation framework.                                                            |
| **LLM Client**              | I created `llm_client.py` as a reusable integration layer between my QA framework and the LLM.                                                          |
| **Prompt Engineering**      | I designed structured, QA-specific prompts that provide the LLM with requirements, test failures, execution results, and clear expected output formats. |
| **Secure Configuration**    | I load the API key securely from `.env` rather than hard-coding credentials in the framework.                                                           |
| **AI Failure Analyzer**     | I created `failure_analyzer.py` to send the test name, error message, and traceback to the LLM for analysis.                                            |
| **Failure Analysis Output** | I use the LLM to identify **probable root cause, recommended fix, and failure category**.                                                               |
| **AI Test Generator**       | I created `test_generator.py` to transform software requirements into structured QA test scenarios.                                                     |
| **Test Scenario Coverage**  | I prompt the LLM to generate **positive, negative, boundary, and edge-case tests**, including test steps and expected results.                          |
| **AI Test Data Generator**  | I created `test_data_generator.py` to generate requirement-based test data.                                                                             |
| **Test Data Coverage**      | I generate **valid, invalid, boundary, and edge-case data** along with expected behavior.                                                               |
| **AI CI Summary**           | I created `ci_summary.py` to convert automated test execution results into a concise QA/CI summary.                                                     |
| **CI Analysis Output**      | I generate **overall test status, important failures, probable causes, release risks, and recommended actions**.                                        |
| **Pytest Integration**      | I created dedicated Pytest integration tests to validate each AI capability.                                                                            |
| **AI Test Coverage**        | I tested the **LLM client, failure analyzer, test generator, test-data generator, and CI summary**.                                                     |
| **Validation Result**       | I successfully executed the complete AI test suite with **5/5 tests passing**.                                                                          |
| **LLM Training**            | I am **not training an LLM from scratch**. I am integrating an existing GPT model through an API and applying prompt engineering for QA use cases.      |
| **Current Status**          | ✅ **AI-Assisted Testing layer complete**                                                                                                                |

```text
                    AI-ASSISTED TESTING
                            │
                    Prompt Engineering
                            │
                       LLM Client
                            │
                     OpenAI / GPT
                            │
        ┌───────────────────┼───────────────────┐
        ↓                   ↓                   ↓
 Failure Analyzer      Test Generator     Test Data Generator
        │                   │                   │
        ↓                   ↓                   ↓
 Root Cause + Fix      Test Scenarios          Test Data


              AUTOMATED TEST RESULTS
                       │
                       ↓
                  AI CI Summary
                       │
                       ↓
               QA / Release Summary
```
