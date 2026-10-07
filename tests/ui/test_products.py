import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_products_page_lists_products(products_page):
    expect(products_page.cards.first).to_be_visible()
    assert products_page.cards.count() > 0


def test_search_shows_results(products_page):
    products_page.search("top")

    expect(products_page.searched_heading).to_be_visible()
    expect(products_page.cards.first).to_be_visible()


def test_search_with_no_match_shows_no_products(products_page):
    products_page.search("zzzzqqqq")

    expect(products_page.searched_heading).to_be_visible()
    expect(products_page.cards).to_have_count(0)
