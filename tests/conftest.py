"""Fixtures shared by UI and API tests."""

import pytest

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
    # Increase default timeout for assertions to handle slow server responses
    playwright.expect_timeout = 15000


# ---------- API clients ----------
@pytest.fixture(scope="session")
def api_context(playwright):
    context = playwright.request.new_context(base_url=settings.api_base_url)
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
