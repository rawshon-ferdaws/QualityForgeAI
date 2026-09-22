def validate_status_code(response, expected_status):
    assert response.status_code == expected_status


def validate_required_fields(data, required_fields):
    for field in required_fields:
        assert field in data


def validate_field_value(data, field, expected_value):
    assert data[field] == expected_value
