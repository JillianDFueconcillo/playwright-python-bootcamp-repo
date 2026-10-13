"""Test Case 14: Place Order: Register while Checkout. See https://automationexercise.com/test_cases"""

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


def test_tc14_place_order_checkout(app, signup_user):
    """Test Case 14: Place Order: Register while Checkout

    Steps from automationexercise.com:
    1. Launch browser
    2. Navigate to url 'http://automationexercise.com'
    3. Verify that home page is visible successfully
    4. Add products to cart
    5. Click 'Cart' button
    6. Verify that cart page is displayed
    7. Click Proceed To Checkout
    8. Click 'Register / Login' button
    9. Fill all details in Signup and create account
    10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    11. Verify ' Logged in as username' at top
    12. Click 'Cart' button
    13. Click 'Proceed To Checkout' button
    14. Verify Address Details and Review Your Order
    15. Enter description in comment text area and click 'Place Order'
    16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    17. Click 'Pay and Confirm Order' button
    18. Verify success message 'Your order has been placed successfully!'
    19. Click 'Delete Account' button
    20. Verify 'ACCOUNT DELETED!' and click 'Continue' button

    NOTE: This test runs with a visible browser window (headed mode) for visual testing.
    The browser_launch_args fixture in conftest.py configures headless=False for this test.
    """
    # STEP 1-2: Launch browser and navigate to the home page (http://automationexercise.com)
    # Opens the base URL configured in pytest.ini or settings
    app.home.open()

    # STEP 3: Verify that home page is visible successfully
    # Checks page title contains 'Automation Exercise' and verifies the slider is visible
    verify_home_page_visible(app)

    # STEP 4: Add products to cart
    # Adds the first featured product and closes the 'Continue Shopping' dialog
    product_name = add_first_product_from_home(app)

    # STEP 5: Click 'Cart' button
    app.nav.cart_link.click()

    # STEP 6: Verify that cart page is displayed
    expect(app.page).to_have_url(re.compile(r"/view_cart"))

    # STEP 7-8: Click Proceed To Checkout, then 'Register / Login' in the guest dialog
    app.cart.proceed_to_checkout()
    app.cart.register_login_link.click()

    # STEP 9-10: Fill signup details, create the account and press Continue
    sign_up_through_ui(app, signup_user)

    # STEP 11: Verify ' Logged in as username' at top
    verify_logged_in_as(app, signup_user["name"])

    # STEP 12-13: Click 'Cart' button, then 'Proceed To Checkout'
    # Logged-in users go straight to the checkout page (no guest dialog)
    app.nav.cart_link.click()
    app.cart.proceed_to_checkout()

    # STEP 14: Verify Address Details and Review Your Order
    verify_address_and_review(app, signup_user, product_name)

    # STEP 15-18: Add a comment, place the order, pay and verify the order is placed
    place_order_and_pay(app, build_card())

    # STEP 19-20: Delete the account and verify ACCOUNT DELETED!
    delete_account_through_ui(app)
