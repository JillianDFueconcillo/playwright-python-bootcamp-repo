"""Test Case 10: Verify Subscription in home page. See https://automationexercise.com/test_cases"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc10_verify_sub_home(app):
    """Test Case 10: Verify Subscription in home page

    Steps from automationexercise.com:
    1. Launch browser
    2. Navigate to url 'http://automationexercise.com'
    3. Verify that home page is visible successfully
    4. Scroll down to footer
    5. Verify text 'SUBSCRIPTION'
    6. Enter email address in input and click arrow button
    7. Verify success message 'You have been successfully subscribed!' is visible

    NOTE: This test runs with a visible browser window (headed mode) for visual testing.
    The browser_launch_args fixture in conftest.py configures headless=False for this test.
    """
    # STEP 1-2: Launch browser and navigate to the home page
    app.home.open()

    # STEP 3: Verify that home page is visible successfully
    verify_home_page_visible(app)

    # STEP 4: Scroll down to footer
    app.home.footer.scroll_into_view()

    # STEP 5: Verify text 'SUBSCRIPTION'
    subscription_heading = app.home.footer.heading
    assert subscription_heading.is_visible()

    # STEP 6: Enter email address in input and click arrow button
    app.home.footer.subscribe("test@example.com")

    # STEP 7: Verify success message 'You have been successfully subscribed!' is visible
    success_message = app.home.footer.success_message
    assert success_message.is_visible()
