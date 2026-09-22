from api.validators import validate_required_fields


def test_order_response_example():
    order = {
        "order_id": 1001,
        "status": "created"
    }

    validate_required_fields(
        order,
        ["order_id", "status"]
    )
