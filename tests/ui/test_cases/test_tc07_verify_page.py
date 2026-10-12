"""Test Case 7: Verify Test Cases Page. See https://automationexercise.com/test_cases"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc07_verify_page(app):
    """Test Case 7: Verify Test Cases Page

    Steps from automationexercise.com:
    1. Launch browser
    2. Navigate to url 'http://automationexercise.com'
    3. Verify that home page is visible successfully
    4. Click on 'Test Cases' button
    5. Verify user is navigated to test cases page successfully

    NOTE: This test runs with a visible browser window (headed mode) for visual testing.
    The browser_launch_args fixture in conftest.py configures headless=False for this test.
    """
    # STEP 1-2: Launch browser and navigate to the home page (http://automationexercise.com)
    # Opens the base URL configured in pytest.ini or settings
    app.home.open()

    # STEP 3: Verify that home page is visible successfully
    # Checks page title contains 'Automation Exercise' and verifies the slider is visible
    verify_home_page_visible(app)

    # STEP 4: Click on 'Test Cases' button in the navigation
    # This navigates user to the test cases page
    app.nav.test_cases_link.click()

    # STEP 5: Verify user is navigated to test cases page successfully
    # Check that the page title contains 'Test Cases'
    assert "Test Cases" in app.page.title(), "Page title should contain 'Test Cases'"

    # Additionally verify the test cases page heading is visible
    assert app.test_cases.heading.is_visible()
