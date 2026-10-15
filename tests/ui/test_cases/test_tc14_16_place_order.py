"""Test Cases 14-16: Place Order variations. See https://automationexercise.com/test_cases

This test is parametrized to run three scenarios:
- TC14: Register during checkout
- TC15: Register before checkout
- TC16: Login before checkout
"""

import re

import pytest
from playwright.sync_api import expect

from autoexercise.data import build_card
from tests.ui.test_cases.steps import (
    add_first_product_from_home,
    delete_account_through_ui,
    place_order_and_pay,
    sign_up_through_ui,
    verify_address_and_review,
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


# ===== Entry functions for each case =====

def _tc14_register_during_checkout(app, user):
    """TC14: Add product first, then register in the checkout dialog."""
    app.home.open()
    verify_home_page_visible(app)
    product_name = add_first_product_from_home(app)
    app.nav.cart_link.click()
    expect(app.page).to_have_url(re.compile(r"/view_cart"))
    app.cart.proceed_to_checkout()
    app.cart.register_login_link.click()
    sign_up_through_ui(app, user)
    verify_logged_in_as(app, user["name"])
    # After signup, we're on home page. Entry ends here; shared tail handles cart/checkout.
    return product_name


def _tc15_register_before_checkout(app, user):
    """TC15: Register from nav, then add product."""
    app.home.open()
    verify_home_page_visible(app)
    app.nav.login_link.click()
    sign_up_through_ui(app, user)
    verify_logged_in_as(app, user["name"])
    product_name = add_first_product_from_home(app)
    # After adding product, we're on home page (modal closed). Shared tail handles cart/checkout.
    return product_name


def _tc16_login_before_checkout(app, user):
    """TC16: Login from nav, then add product."""
    app.home.open()
    verify_home_page_visible(app)
    app.nav.login_link.click()
    app.login.login(user["email"], user["password"])
    verify_logged_in_as(app, user["name"])
    product_name = add_first_product_from_home(app)
    # After adding product, we're on home page (modal closed). Shared tail handles cart/checkout.
    return product_name


# ===== Parametrized test =====

@pytest.mark.parametrize(
    "fixture_name,entry_func",
    [
        pytest.param("signup_user", _tc14_register_during_checkout, id="tc14"),
        pytest.param("signup_user", _tc15_register_before_checkout, id="tc15"),
        pytest.param("new_user", _tc16_login_before_checkout, id="tc16"),
    ],
)
def test_place_order(app, request, fixture_name, entry_func):
    """Parametrized checkout test covering TC14, TC15, and TC16.

    Each variant has different entry steps but shares the same checkout tail.

    NOTE: This test runs with a visible browser window (headed mode) for visual testing.
    The browser_launch_args fixture in conftest.py configures headless=False for this test.
    """
    # Get the appropriate user fixture dynamically
    user = request.getfixturevalue(fixture_name)

    # Run the entry steps specific to this case (register during, register before, or login)
    product_name = entry_func(app, user)

    # ===== Shared checkout steps for all three cases =====

    # After entry, we're on the home page. Go to cart first.
    app.nav.cart_link.click()

    # Click Proceed To Checkout
    app.cart.proceed_to_checkout()

    # Verify Address Details and Review Your Order
    verify_address_and_review(app, user, product_name)

    # Add comment, place order, pay and verify
    place_order_and_pay(app, build_card())

    # Delete account and verify
    delete_account_through_ui(app)
