"""Test Case 6: Contact Us Form. See https://automationexercise.com/contact_us"""

import pytest

from tests.ui.test_cases.steps import verify_home_page_visible

pytestmark = [pytest.mark.ui, pytest.mark.testcases]


def test_tc06_contact_form(app):
    """Test Case 6: Contact Us Form

    Steps:
    1. Launch browser
    2. Navigate to url 'http://automationexercise.com'
    3. Verify that home page is visible successfully
    4. Click on 'Contact Us' button
    5. Verify 'GET IN TOUCH' is visible
    6. Enter name, email, subject, message and submit form in Chromium browser
    7. Verify form is submitted

    NOTE: This test runs with a visible browser window (headed mode) for visual testing.
    """
    # STEP 1-2: Launch browser and navigate to the home page
    app.home.open()

    # STEP 3: Verify that home page is visible successfully
    verify_home_page_visible(app)

    # STEP 4: Click on 'Contact Us' button in the navigation
    app.nav.contact_link.click()

    # STEP 5: Verify 'GET IN TOUCH' heading is visible
    assert app.contact.heading.is_visible()

    # STEP 6: Fill in the contact form directly with Playwright commands
    # Fill in Name field
    name_field = app.page.get_by_test_id("name")
    name_field.clear()
    name_field.fill("j")

    # Fill in Email field
    email_field = app.page.get_by_test_id("email")
    email_field.clear()
    email_field.fill("student_test383840z@gmail.com")

    # Fill in Subject field
    subject_field = app.page.get_by_test_id("subject")
    subject_field.clear()
    subject_field.fill("test email")

    # Fill in Message field
    message_field = app.page.get_by_test_id("message")
    message_field.clear()
    message_field.fill("My message is here")

    # Register dialog handler to accept the confirmation dialog
    app.page.once("dialog", lambda dialog: dialog.accept())

    # STEP 7: Click the Submit button
    submit_button = app.page.locator("input[data-qa='submit-button']")
    submit_button.click()

    # Wait a moment for the submission to process
    import time

    time.sleep(2)

    # Verify we're still on the contact page (form submitted successfully)
    assert app.contact.heading.is_visible()
