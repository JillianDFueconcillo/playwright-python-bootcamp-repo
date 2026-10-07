import pytest

from autoexercise.api.base_client import code

pytestmark = pytest.mark.api


@pytest.mark.smoke
def test_list_products(catalog_api):
    response = catalog_api.list_products()

    assert code(response) == 200
    products = response.json()["products"]
    assert len(products) > 0
    assert {"id", "name", "price", "brand", "category"} <= products[0].keys()


def test_post_to_products_list_is_not_supported(catalog_api):
    response = catalog_api.post("productsList")

    assert code(response) == 405


def test_list_brands(catalog_api):
    response = catalog_api.list_brands()

    assert code(response) == 200
    assert len(response.json()["brands"]) > 0


def test_search_products(catalog_api):
    response = catalog_api.search_products("top")

    assert code(response) == 200
    assert len(response.json()["products"]) > 0


def test_search_without_term_is_a_bad_request(catalog_api):
    response = catalog_api.search_products()

    assert code(response) == 400
