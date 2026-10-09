"""Test Case 4: Logout User. See https://automationexercise.com/test_cases"""

# Import pytest framework for test marking and fixtures
import pytest

# Import reusable helper functions from steps module that are used across multiple test cases
from tests.ui.test_cases.steps import (
    verify_home_page_visible,  # Helper function to verify home page is loaded correctly
    verify_logged_in_as,  # Helper function to verify user is logged in with correct name
)

# Mark all tests in this module with 'ui' and 'testcases' pytest markers
# These markers allow filtering tests: pytest -m ui, pytest -m testcases
pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc04_logout_user(app, new_user):
    """Test Case 4: Logout User.
    
    Steps from automationexercise.com:
    1. Launch browser
    2. Navigate to url 'http://automationexercise.com'
    3. Verify that home page is visible successfully
    4. Click on 'Signup / Login' button
    5. Verify 'Login to your account' is visible
    6. Enter correct email address and password
    7. Click 'login' button
    8. Verify that 'Logged in as username' is visible
    9. Click 'Logout' button
    10. Verify that user is navigated to login page
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
    
    # STEPS 6-7: Enter correct email address and password, then click login button
    # Uses the new_user fixture which provides pre-created account credentials
    # The login() method fills email, password fields and clicks the login button
    app.login.login(new_user["email"], new_user["password"])
    
    # STEP 8: Verify that 'Logged in as username' is visible in the header
    # Confirms successful login by checking if the user's name appears in navigation
    verify_logged_in_as(app, new_user["name"])
    
    # STEP 9: Click 'Logout' button in the navigation bar
    # This logs out the user and clears the session
    app.nav.logout_link.click()
    
    # STEP 10: Verify that user is navigated to login page
    # After logout, the login heading should be visible and logged in indicator should disappear
    assert app.login.login_heading.is_visible(), "Should be on login page after logout"
    assert app.nav.logged_in_as.count() == 0, "User should not be logged in anymore"
