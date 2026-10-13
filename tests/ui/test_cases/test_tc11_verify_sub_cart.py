"""Test Case 11: Verify Subscription in Cart page. See https://automationexercise.com/test_cases"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc11_verify_sub_cart(app):
    """Test Case 11: Verify Subscription in Cart page

    Steps from automationexercise.com:
    1. Launch browser
    2. Navigate to url 'http://automationexercise.com'
    3. Verify that home page is visible successfully
    4. Click 'Cart' button
    5. Scroll down to footer
    6. Verify text 'SUBSCRIPTION'
    7. Enter email address in input and click arrow button
    8. Verify success message 'You have been successfully subscribed!' is visible

    NOTE: This test runs with a visible browser window (headed mode) for visual testing.
    The browser_launch_args fixture in conftest.py configures headless=False for this test.
    """
    # STEP 1-2: Launch browser and navigate to the home page
    app.home.open()

    # STEP 3: Verify that home page is visible successfully
    verify_home_page_visible(app)

    # STEP 4: Click 'Cart' button
    app.nav.cart_link.click()

    # STEP 5: Scroll down to footer
    app.footer.scroll_into_view()

    # STEP 6: Verify text 'SUBSCRIPTION'
    subscription_heading = app.footer.heading
    assert subscription_heading.is_visible()

    # STEP 7: Enter email address in input and click arrow button
    app.footer.subscribe("test@example.com")

    # STEP 8: Verify success message 'You have been successfully subscribed!' is visible
    success_message = app.footer.success_message
    assert success_message.is_visible()
