import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_added_product_appears_in_cart(products_page, cart_page):
    expect(products_page.cards.first).to_be_visible()
    name = products_page.names.first.inner_text()

    products_page.add_to_cart(index=0)
    cart_page.open()

    expect(cart_page.rows).to_have_count(1)
    expect(cart_page.item_names.first).to_have_text(name)
