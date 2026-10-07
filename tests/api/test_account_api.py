import pytest

from autoexercise.api.base_client import code
from autoexercise.data import build_user

pytestmark = pytest.mark.api


@pytest.mark.smoke
def test_verify_login_with_valid_credentials(account_api, new_user):
    response = account_api.verify_login(new_user["email"], new_user["password"])

    assert code(response) == 200
    assert response.json()["message"] == "User exists!"


def test_verify_login_with_wrong_password(account_api, new_user):
    response = account_api.verify_login(new_user["email"], "wrong-password")

    assert code(response) == 404
    assert response.json()["message"] == "User not found!"


def test_verify_login_without_email_is_a_bad_request(account_api):
    response = account_api.verify_login(password="whatever")

    assert code(response) == 400


def test_create_and_delete_account(account_api):
    user = build_user()

    created = account_api.create(user)
    assert code(created) == 201
    assert created.json()["message"] == "User created!"

    deleted = account_api.delete_account(user["email"], user["password"])
    assert code(deleted) == 200
    assert deleted.json()["message"] == "Account deleted!"


def test_get_user_detail_by_email(account_api, new_user):
    response = account_api.get_by_email(new_user["email"])

    assert code(response) == 200
    assert response.json()["user"]["name"] == new_user["name"]
