"""Test Case 16: Place Order: Login before Checkout. See https://automationexercise.com/test_cases"""

import re

import pytest
from playwright.sync_api import expect

from autoexercise.data import build_card
from tests.ui.test_cases.steps import (
    add_first_product_from_home,
    delete_account_through_ui,
    place_order_and_pay,
    verify_address_and_review,
    verify_home_page_visible,
    verify_logged_in_as,
)

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc16_login_before_checkout(app, new_user):
    """Test Case 16: Place Order: Login before Checkout

    Steps from automationexercise.com:
    1. Launch browser
    2. Navigate to url 'http://automationexercise.com'
    3. Verify that home page is visible successfully
    4. Click 'Signup / Login' button
    5. Fill email, password and click 'Login' button
    6. Verify 'Logged in as username' at top
    7. Add products to cart
    8. Click 'Cart' button
    9. Verify that cart page is displayed
    10. Click Proceed To Checkout
    11. Verify Address Details and Review Your Order
    12. Enter description in comment text area and click 'Place Order'
    13. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    14. Click 'Pay and Confirm Order' button
    15. Verify success message 'Your order has been placed successfully!'
    16. Click 'Delete Account' button
    17. Verify 'ACCOUNT DELETED!' and click 'Continue' button

    NOTE: This test runs with a visible browser window (headed mode) for visual testing.
    The browser_launch_args fixture in conftest.py configures headless=False for this test.
    """
    # STEP 1-2: Launch browser and navigate to the home page (http://automationexercise.com)
    # Opens the base URL configured in pytest.ini or settings
    app.home.open()

    # STEP 3: Verify that home page is visible successfully
    # Checks page title contains 'Automation Exercise' and verifies the slider is visible
    verify_home_page_visible(app)

    # STEP 4: Click 'Signup / Login' button in the navigation bar
    app.nav.login_link.click()

    # STEP 5: Fill email, password and click 'Login' button
    # new_user is an account that already exists on the site (created through the API)
    app.login.login(new_user["email"], new_user["password"])

    # STEP 6: Verify 'Logged in as username' at top
    verify_logged_in_as(app, new_user["name"])

    # STEP 7: Add products to cart
    # Adds the first featured product and closes the 'Continue Shopping' dialog
    product_name = add_first_product_from_home(app)

    # STEP 8: Click 'Cart' button
    app.nav.cart_link.click()

    # STEP 9: Verify that cart page is displayed
    expect(app.page).to_have_url(re.compile(r"/view_cart"))

    # STEP 10: Click Proceed To Checkout
    app.cart.proceed_to_checkout()

    # STEP 11: Verify Address Details and Review Your Order
    verify_address_and_review(app, new_user, product_name)

    # STEP 12-15: Add a comment, place the order, pay and verify the order is placed
    place_order_and_pay(app, build_card())

    # STEP 16-17: Delete the account and verify ACCOUNT DELETED!
    delete_account_through_ui(app)
