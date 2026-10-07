"""Reusable steps shared by the numbered test cases.

Each function matches a step that repeats across the test cases on
https://automationexercise.com/test_cases
"""

import re

from autoexercise.pages.app import App


def verify_home_page_visible(app: App) -> None:
    """'Verify that home page is visible successfully'"""
    title = app.page.title()
    assert re.search(r"Automation Exercise", title), f"Expected title to contain 'Automation Exercise', got '{title}'"
    assert app.home.slider.is_visible(), "Home slider should be visible"


def sign_up_through_ui(app: App, user: dict) -> None:
    """Start signup, fill the account form, create the account, press Continue."""
    app.login.start_signup(user["name"], user["email"])
    assert app.signup.account_info_heading.is_visible(), "Account info heading should be visible"
    app.signup.fill_account(user)
    app.signup.submit()
    heading_text = app.account.created_heading.inner_text()
    assert re.search(r"account created", heading_text, re.IGNORECASE), f"Expected 'account created' in '{heading_text}'"
    app.account.continue_button.click()


def verify_logged_in_as(app: App, name: str) -> None:
    """'Verify that Logged in as username is visible'"""
    logged_in_text = app.nav.logged_in_as.inner_text()
    assert name in logged_in_text, f"Expected '{name}' in '{logged_in_text}'"


def delete_account_through_ui(app: App) -> None:
    """Click Delete Account, verify ACCOUNT DELETED!, press Continue."""
    app.nav.delete_account_link.click()
    deleted_text = app.account.deleted_heading.inner_text()
    assert re.search(r"account deleted", deleted_text, re.IGNORECASE), f"Expected 'account deleted' in '{deleted_text}'"
    app.account.continue_button.click()


def add_first_product_from_home(app: App) -> str:
    """Add the first featured product to the cart and return its name."""
    assert app.home.featured_items.first.is_visible(), "First featured item should be visible"
    name = app.home.featured_items.first.locator(".productinfo p").inner_text()
    app.home.add_card_to_cart(app.home.featured_items.first)
    app.home.continue_shopping()
    return name


def verify_address_and_review(app: App, user: dict, product_name: str) -> None:
    """'Verify Address Details and Review Your Order'"""
    delivery_text = app.checkout.delivery_address.inner_text()
    for field in ("firstname", "lastname", "address1", "city", "country", "mobile_number"):
        assert user[field] in delivery_text, f"Expected '{user[field]}' in delivery address"
    order_text = app.checkout.order_review.inner_text()
    assert product_name in order_text, f"Expected '{product_name}' in order review"


def place_order_and_pay(
    app: App, card: dict, comment: str = "Please deliver in the morning"
) -> None:
    """Comment, Place Order, payment details, Pay and Confirm Order, verify the result.

    The site flashes 'Your order has been placed successfully!' and then moves to the
    'Order Placed!' page. The flash disappears fast, so the test verifies the final page.
    """
    app.checkout.place_order(comment)
    app.payment.pay(card)
    heading_text = app.order.heading.inner_text()
    assert re.search(r"order placed", heading_text, re.IGNORECASE), f"Expected 'order placed' in '{heading_text}'"
    confirmation = app.page.get_by_text("Congratulations! Your order has been confirmed!")
    assert confirmation.is_visible(), "Order confirmation message should be visible"
