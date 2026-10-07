import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_valid_login_shows_user_name(login_page, new_user):
    login_page.login(new_user["email"], new_user["password"])

    expect(login_page.nav.logged_in_as).to_contain_text(new_user["name"])
    expect(login_page.nav.logout_link).to_be_visible()


def test_wrong_password_shows_error(login_page, new_user):
    login_page.login(new_user["email"], "wrong-password")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.nav.logged_in_as).to_have_count(0)
