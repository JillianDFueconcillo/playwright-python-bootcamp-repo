"""Test data builders. Every call returns a brand new, unique user."""

import uuid


def build_email() -> str:
    return f"qa.{uuid.uuid4().hex[:10]}@example.com"


def build_card() -> dict:
    """Any card data is accepted by the practice site."""
    return {
        "name": "Test User",
        "number": "4111111111111111",
        "cvc": "123",
        "expiry_month": "12",
        "expiry_year": "2030",
    }


def build_user(**overrides) -> dict:
    token = uuid.uuid4().hex[:10]
    user = {
        "name": f"Tester{token}",
        "email": f"qa.{token}@example.com",
        "password": "Passw0rd!",
        "title": "Mrs",
        "birth_date": "10",
        "birth_month": "May",
        "birth_year": "1990",
        "firstname": "Test",
        "lastname": "User",
        "company": "Bootcamp",
        "address1": "1 Main Street",
        "address2": "Suite 2",
        "country": "United States",
        "zipcode": "10001",
        "state": "NY",
        "city": "New York",
        "mobile_number": "5551234567",
    }
    user.update(overrides)
    return user
