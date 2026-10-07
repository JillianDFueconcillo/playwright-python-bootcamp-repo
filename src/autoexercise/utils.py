import re


def parse_price(text: str) -> int:
    """'Rs. 1,500' -> 1500"""
    digits = re.sub(r"[^\d]", "", text)
    return int(digits)
