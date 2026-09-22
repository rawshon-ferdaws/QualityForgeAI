from api.validators import validate_field_value


def test_product_response_example():
    product = {
        "id": 1,
        "name": "Sauce Labs Backpack"
    }

    validate_field_value(
        product,
        "name",
        "Sauce Labs Backpack"
    )
