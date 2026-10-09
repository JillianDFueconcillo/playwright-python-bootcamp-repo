"""Fixtures shared by UI and API tests."""

import pytest
import time

from autoexercise.api.account_client import AccountClient
from autoexercise.api.base_client import code
from autoexercise.api.catalog_client import CatalogClient
from autoexercise.config import settings
from autoexercise.data import build_user


@pytest.fixture(scope="session")
def base_url() -> str:
    """Overrides the pytest-base-url fixture so page.goto('/x') uses our config."""
    return settings.ui_base_url


@pytest.fixture(scope="session", autouse=True)
def use_data_qa_attribute(playwright):
    """The site marks form elements with data-qa, so get_by_test_id reads that attribute."""
    playwright.selectors.set_test_id_attribute("data-qa")
    # Increase default timeout for assertions to handle slow server responses and WAF verification
    playwright.expect_timeout = 30000  # 30 seconds instead of 5 to handle WAF blocks


@pytest.fixture(autouse=True)
def rate_limit_delay():
    """Add a small delay between tests to avoid WAF rate limiting.
    
    GitHub Actions runners often share IPs, which can trigger rate limits
    when running tests rapidly.
    """
    yield
    time.sleep(0.2)  # 200ms between tests


# ---------- API clients ----------
@pytest.fixture(scope="session")
def api_context(playwright):
    """Create API context with browser-like headers to avoid WAF blocking."""
    context = playwright.request.new_context(
        base_url=settings.api_base_url,
        extra_http_headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Cache-Control": "max-age=0",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        },
    )
    yield context
    context.dispose()


@pytest.fixture(scope="session")
def catalog_api(api_context) -> CatalogClient:
    return CatalogClient(api_context)


@pytest.fixture(scope="session")
def account_api(api_context) -> AccountClient:
    return AccountClient(api_context)


# ---------- test data ----------
@pytest.fixture
def new_user(account_api):
    """A real account created through the API and deleted after the test."""
    user = build_user()
    created = account_api.create(user)
    assert code(created) == 201, created.text()
    yield user
    account_api.delete_account(user["email"], user["password"])
