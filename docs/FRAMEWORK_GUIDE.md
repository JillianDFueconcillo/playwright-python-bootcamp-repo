# Framework Guide

## The layers

```
tests/            What to check. Short, readable, no locators, no URLs.
   |
   +-- pages/     How to drive the browser. One class per page.
   +-- api/       How to call the service. One class per resource group.
   |
config.py, data.py   Where things live and how test data is built.
```

A test reads like a sentence:

```python
def test_valid_login_shows_user_name(login_page, new_user):
    login_page.login(new_user["email"], new_user["password"])
    expect(login_page.nav.logged_in_as).to_contain_text(new_user["name"])
```

## Fixtures

Fixtures live in `tests/conftest.py` (shared) and `tests/ui/conftest.py` (UI only). Pytest injects them by argument name.

| Fixture | Scope | What you get |
| --- | --- | --- |
| `page` | test | Browser page with ads blocked (wraps the pytest-playwright page) |
| `home_page`, `login_page`, `products_page` | test | Page object, already opened |
| `cart_page` | test | Page object, not opened |
| `api_context` | session | One Playwright HTTP context for all API tests |
| `catalog_api`, `account_api` | session | API clients |
| `new_user` | test | A real user created through the API, deleted after the test |
| `app` | test | Every page object in one handle (`app.home`, `app.cart`, ...). Opens nothing. |
| `signup_user` | test | Unique user data for tests that register through the browser. Cleaned up through the API |

Scope matters. Session scope runs once per test run. Test scope runs once per test. Browser state stays test scoped so tests stay independent.

## The app fixture

Long flows touch many pages. The `app` fixture gives one object with all page objects, so a test reads from top to bottom:

```python
app.home.open()
app.nav.login_link.click()
app.login.login(user["email"], user["password"])
```

Use `home_page`, `login_page`, and the other single page fixtures for short tests that start on one page. Use `app` when a test crosses pages. Shared steps such as "sign up" and "delete account" sit in `tests/ui/test_cases/steps.py`.

## Test data

`build_user()` in `src/autoexercise/data.py` returns a user with a unique email each time. The public site is shared, so unique data prevents collisions with other students. The `new_user` fixture creates the account before the test and deletes it after, even if the test fails.

## Page objects

Rules:

- Locators are properties. Actions are methods.
- Methods do not assert. Tests assert.
- Prefer `get_by_role`, `get_by_label`, `get_by_text`, and `get_by_test_id`. This site marks forms with `data-qa`, and `conftest.py` tells Playwright to use that attribute for `get_by_test_id`. Where no good attribute exists, a short CSS selector is fine.

To add a page:

1. Create `src/autoexercise/pages/<name>_page.py` and extend `BasePage`.
2. Set `path` if the page has its own URL.
3. Add a fixture in `tests/ui/conftest.py`.

## API clients

`BaseClient` wraps Playwright's `APIRequestContext`. Each resource group gets a small class:

```python
class CatalogClient(BaseClient):
    def list_products(self):
        return self.get("productsList")
```

Rules:

- Clients return the raw response. Tests decide what to assert.
- Paths have no leading slash. The base URL is `https://automationexercise.com/api/`, and a leading slash would drop `/api`.
- Request bodies are form encoded (`form=`), not JSON. The API expects it.
- The result code is in the body. Assert with `code(response)`.

To add a client:

1. Create `src/autoexercise/api/<name>_client.py` and extend `BaseClient`.
2. Add a fixture in `tests/conftest.py`.
3. Read the endpoint at https://automationexercise.com/api_list.

## Configuration

`src/autoexercise/config.py` reads environment variables with public defaults. See `.env.example`.

## Markers

Declared in `pytest.ini`. An unknown marker produces a warning, so declare new ones there.

| Marker | Use |
| --- | --- |
| `smoke` | Fast checks of the main paths |
| `ui`, `api` | Layer |
| `regression` | Broader checks |
| `exercise` | Student exercises. CI skips them. Remove the marker when the exercise is done |

## Failure evidence

`pytest.ini` turns on screenshots and traces for failures. Open a trace with `playwright show-trace`. The trace shows every action, the DOM at each step, network calls, and console messages.

## Why Playwright for the API layer

One tool to learn. The same runner, config, and reports cover UI and API tests. You can mix them in one test, for example create a user through the API and log in through the browser.
