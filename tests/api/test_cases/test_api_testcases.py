"""API counterparts of the numbered test cases on https://automationexercise.com/test_cases

Only the test cases with a matching API endpoint appear here. The others are UI only.
See docs/TEST_CASES.md for the full table.

TC01 Register User                  -> createAccount, getUserDetailByEmail, deleteAccount
TC02 Login with correct credentials -> verifyLogin
TC03 Login with wrong credentials   -> verifyLogin
TC05 Register with existing email   -> createAccount
TC08 All products and product data  -> productsList
TC09 Search product                 -> searchProduct
TC18 Category products              -> productsList (category data)
TC19 Brand products                 -> brandsList, productsList (brand data)
TC20 Search products (search part)  -> searchProduct
"""

import pytest

from autoexercise.api.base_client import code
from autoexercise.data import build_user

pytestmark = [pytest.mark.api, pytest.mark.testcases]


@pytest.fixture(scope="module")
def all_products(catalog_api) -> list[dict]:
    response = catalog_api.list_products()
    assert code(response) == 200
    return response.json()["products"]


def test_tc01_register_user_api(account_api):
    user = build_user()

    created = account_api.create(user)
    assert code(created) == 201
    assert created.json()["message"] == "User created!"

    detail = account_api.get_by_email(user["email"])
    assert code(detail) == 200
    assert detail.json()["user"]["name"] == user["name"]

    deleted = account_api.delete_account(user["email"], user["password"])
    assert code(deleted) == 200
    assert deleted.json()["message"] == "Account deleted!"

    assert code(account_api.get_by_email(user["email"])) == 404


def test_tc02_login_with_correct_credentials_api(account_api, new_user):
    response = account_api.verify_login(new_user["email"], new_user["password"])

    assert code(response) == 200
    assert response.json()["message"] == "User exists!"


def test_tc03_login_with_incorrect_credentials_api(account_api, new_user):
    response = account_api.verify_login(new_user["email"], "wrong-password")

    assert code(response) == 404
    assert response.json()["message"] == "User not found!"


def test_tc05_register_with_existing_email_api(account_api, new_user):
    duplicate = build_user(email=new_user["email"])

    response = account_api.create(duplicate)

    assert code(response) == 400


def test_tc08_products_data_api(all_products):
    """The API has name, price, brand and category. Availability and condition are UI only."""
    assert len(all_products) > 0
    for product in all_products:
        assert product["name"]
        assert product["price"].startswith("Rs.")
        assert product["brand"]
        assert product["category"]["category"]


def test_tc09_search_product_api(catalog_api):
    response = catalog_api.search_products("jeans")

    assert code(response) == 200
    names = [p["name"].lower() for p in response.json()["products"]]
    assert names
    assert all("jeans" in name for name in names)


def test_tc18_category_data_api(all_products):
    user_types = {p["category"]["usertype"]["usertype"] for p in all_products}

    assert {"Women", "Men"} <= user_types
    women_tops = [
        p for p in all_products
        if p["category"]["usertype"]["usertype"] == "Women" and p["category"]["category"] == "Tops"
    ]
    assert women_tops, "expected products in Women > Tops"


def test_tc19_brand_data_api(catalog_api, all_products):
    response = catalog_api.list_brands()
    assert code(response) == 200
    brands = {b["brand"] for b in response.json()["brands"]}
    assert len(brands) >= 2

    brands_with_products = {p["brand"] for p in all_products}
    assert brands_with_products <= brands, "every product brand should be a listed brand"


def test_tc20_search_results_api(catalog_api):
    """The search half of TC20. The cart and login halves need the browser."""
    response = catalog_api.search_products("jeans")

    assert code(response) == 200
    assert len(response.json()["products"]) > 0
