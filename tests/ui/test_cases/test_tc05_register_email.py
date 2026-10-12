"""Test Case 5: Register User with existing email. See https://automationexercise.com/test_cases"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc05_register_email(app, new_user):
    """Test Case 5: Register User with existing email

    Steps from automationexercise.com:
    1. Launch browser
    2. Navigate to url 'http://automationexercise.com'
    3. Verify that home page is visible successfully
    4. Click on 'Signup / Login' button
    5. Verify 'New User Signup!' is visible
    6. Enter name and already registered email address
    7. Click 'Signup' button
    8. Verify error 'Email Address already exist!' is visible
    """
    # STEP 1-2: Launch browser and navigate to the home page (http://automationexercise.com)
    # Opens the base URL configured in pytest.ini or settings
    app.home.open()

    # STEP 3: Verify that home page is visible successfully
    # Checks page title contains 'Automation Exercise' and verifies the slider is visible
    verify_home_page_visible(app)

    # STEP 4: Click on 'Signup / Login' button in the navigation bar
    # This navigates user to the login/signup page
    app.nav.login_link.click()

    # STEP 5: Verify 'New User Signup!' heading is visible
    # Ensures the signup form is displayed (as opposed to login form)
    assert app.login.signup_heading.is_visible()

    # STEPS 6-7: Enter name and already registered email address, then click signup button
    # Uses the new_user fixture which provides an email that already exists
    # The start_signup() method fills name, email fields and clicks the signup button
    app.login.start_signup(new_user["name"], new_user["email"])

    # STEP 8: Verify error 'Email Address already exist!' is visible
    # Confirms that the signup failed with the expected error message for duplicate email
    assert app.login.signup_error.is_visible()
