import re

import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_home_page_shows_featured_products(home_page):
    expect(home_page.page).to_have_title(re.compile("Automation Exercise"))
    expect(home_page.featured_items.first).to_be_visible()


def test_guest_sees_login_link(home_page):
    expect(home_page.nav.login_link).to_be_visible()
    expect(home_page.nav.logged_in_as).to_have_count(0)
