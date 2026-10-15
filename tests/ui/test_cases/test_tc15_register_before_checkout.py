"""Test Case 15: Place Order: Register before Checkout. See https://automationexercise.com/test_cases"""

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


def test_tc15_register_before_checkout(app, signup_user):
    """Test Case 15: Place Order: Register before Checkout

    Steps from automationexercise.com:
    1. Launch browser
    2. Navigate to url 'http://automationexercise.com'
    3. Verify that home page is visible successfully
    4. Click 'Signup / Login' button
    5. Fill all details in Signup and create account
    6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    7. Verify ' Logged in as username' at top
    8. Add products to cart
    9. Click 'Cart' button
    10. Verify that cart page is displayed
    11. Click Proceed To Checkout
    12. Verify Address Details and Review Your Order
    13. Enter description in comment text area and click 'Place Order'
    14. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    15. Click 'Pay and Confirm Order' button
    16. Verify success message 'Your order has been placed successfully!'
    17. Click 'Delete Account' button
    18. Verify 'ACCOUNT DELETED!' and click 'Continue' button

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

    # STEP 5-6: Fill signup details, create the account and press Continue
    sign_up_through_ui(app, signup_user)

    # STEP 7: Verify ' Logged in as username' at top
    verify_logged_in_as(app, signup_user["name"])

    # STEP 8: Add products to cart
    # Adds the first featured product and closes the 'Continue Shopping' dialog
    product_name = add_first_product_from_home(app)

    # STEP 9: Click 'Cart' button
    app.nav.cart_link.click()

    # STEP 10: Verify that cart page is displayed
    expect(app.page).to_have_url(re.compile(r"/view_cart"))

    # STEP 11: Click Proceed To Checkout
    # Logged-in users go straight to the checkout page (no guest dialog)
    app.cart.proceed_to_checkout()

    # STEP 12: Verify Address Details and Review Your Order
    verify_address_and_review(app, signup_user, product_name)

    # STEP 13-16: Add a comment, place the order, pay and verify the order is placed
    place_order_and_pay(app, build_card())

    # STEP 17-18: Delete the account and verify ACCOUNT DELETED!
    delete_account_through_ui(app)
