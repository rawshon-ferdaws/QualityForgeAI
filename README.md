Project Architecture / Current Framework Summary

| Area                   | What We Are Applying                                                                                                                                                                                  |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purpose of Testing** | To verify that the application works correctly across **UI, API, and backend layers**, catch defects early, validate critical user workflows, and ensure reliable releases through automated testing. |
| **What We Are Doing**  | Automating **positive, negative, regression, integration, and E2E scenarios** using reusable framework components.                                                                                    |
| **Selenium**           | UI automation using **Page Object Model (POM)**, locators, explicit waits, reusable actions, and browser automation.                                                                                  |
| **Browser**            | **Firefox — current stable execution browser.** Chrome is supported but currently has a Chrome/WebDriver stability issue in our environment.                                                          |
| **Pytest**             | Test execution, fixtures, assertions, markers, test organization, setup and teardown.                                                                                                                 |
| **API**                | API automation using **Python Requests** — GET, POST, PUT/PATCH, DELETE, payloads, parameters, headers, and response validation.                                                                      |
| **Database**           | **SQL-based** backend/data validation.                                                                                                                                                                |
| **CI/CD Pipeline**     | **GitHub Actions** for automated test execution on code changes.                                                                                                                                      |
| **Docker**             | Reproducible and consistent test execution environment.                                                                                                                                               |
| **AI Pipeline**        | LLM-assisted **failure analysis, test generation, test-data generation, and CI test summaries**.                                                                                                      |
| **LLM**                | **Yes** — existing LLM integration for AI-assisted QA.                                                                                                                                                |
| **LLM Trainer**        | **No** — we are not training an LLM from scratch.                                                                                                                                                     |
| **Current Status**     | **UI automation complete — 18/18 tests passing** across Login, Products, Cart, Checkout, and E2E purchase flow.                                                                                       |

UI Testing — Selenium + POM Automation

| Point                  | What We Applied                                                                                                                |
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

API Testing — Python Requests + Pytest

| Point                        | What We Applied                                                                                                                              |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purpose**                  | Verify that backend APIs return the correct **status codes, headers, response data, structure, and data types** without depending on the UI. |
| **Framework**                | **Python + Requests + Pytest** API automation framework.                                                                                     |
| **API Used**                 | **JSONPlaceholder REST API** for API automation practice.                                                                                    |
| **API Client**               | Created reusable `APIClient` methods for **GET, POST, PUT, PATCH, and DELETE** requests.                                                     |
| **Endpoints**                | Centralized API endpoints in `endpoints.py` instead of hardcoding URLs throughout tests.                                                     |
| **Configuration**            | API base URL and timeout managed through **`config.ini`**.                                                                                   |
| **Test Data**                | Request payloads externalized into **`api_payloads.json`**.                                                                                  |
| **GET Testing**              | Tested **single user, all users, posts, and query-parameter filtering**.                                                                     |
| **POST Testing**             | Tested creation requests and validated the returned response.                                                                                |
| **PUT Testing**              | Tested complete resource-update requests.                                                                                                    |
| **PATCH Testing**            | Tested partial resource updates.                                                                                                             |
| **DELETE Testing**           | Tested delete requests and expected response status.                                                                                         |
| **Query Parameters**         | Tested filtering resources using parameters such as **`userId`**.                                                                            |
| **Status Code Validation**   | Validated expected codes including **200, 201, and 404**.                                                                                    |
| **Header Validation**        | Verified the response **Content-Type** is JSON.                                                                                              |
| **Response Body Validation** | Validated response **keys, values, and data types**.                                                                                         |
| **Reusable Validators**      | Created reusable validation methods in **`validators.py`**.                                                                                  |
| **Positive Testing**         | Tested valid GET/POST/PUT/PATCH/DELETE requests and expected responses.                                                                      |
| **Negative Testing**         | Tested requests for **nonexistent users/posts** and validated **404** responses.                                                             |
| **Functional Testing**       | Verified that individual REST operations behave according to their expected API behavior.                                                    |
| **Contract Testing**         | Validated the API response contract using **JSON Schema** in `user_schema.json`.                                                             |
| **Schema Validation**        | Checked required fields such as `id`, `name`, `username`, `email`, `address`, etc., and their expected types.                                |
| **Regression Testing**       | API tests can be rerun as a suite to detect whether existing API behavior has changed.                                                       |
| **Smoke Testing**            | Critical API checks such as GET user/resource availability can form a smaller fast validation suite.                                         |
| **Risk-Based Testing**       | Focused validation on important API behavior: successful requests, response integrity, errors, and API contract.                             |
| **Shift-Left Testing**       | API tests can execute independently of UI tests and are designed to be integrated into **CI/CD** for earlier defect detection.               |
| **API Result**               | **17 API tests passing** in the combined project run.                                                                                        |
