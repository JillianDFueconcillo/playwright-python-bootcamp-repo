"""Test Case 3: Login User with incorrect email and password. See https://automationexercise.com/test_cases"""

# Import pytest framework for test marking and fixtures
import pytest

# Import reusable helper functions from steps module that are used across multiple test cases
from tests.ui.test_cases.steps import (
    verify_home_page_visible,  # Helper function to verify home page is loaded correctly
)

# Mark all tests in this module with 'ui' and 'testcases' pytest markers
# These markers allow filtering tests: pytest -m ui, pytest -m testcases
pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc03_login_user_incorrect(app, new_user):
    """Test Case 3: Login User with incorrect email and password.
    
    Steps from automationexercise.com:
    1. Launch browser
    2. Navigate to url 'http://automationexercise.com'
    3. Verify that home page is visible successfully
    4. Click on 'Signup / Login' button
    5. Verify 'Login to your account' is visible
    6. Enter incorrect email address and password
    7. Click 'login' button
    8. Verify error 'Your email or password is incorrect!' is visible
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
    
    # STEP 5: Verify 'Login to your account' heading is visible
    # Ensures the login form is displayed (as opposed to signup form)
    assert app.login.login_heading.is_visible()
    
    # STEPS 6-7: Enter incorrect email address and password, then click login button
    # Uses the new_user fixture but with wrong password intentionally
    # The login() method fills email, incorrect password fields and clicks the login button
    app.login.login(new_user["email"], "wrong-password-12345")
    
    # STEP 8: Verify error 'Your email or password is incorrect!' is visible
    # Confirms that the login failed with the expected error message
    assert app.login.error_message.is_visible()
