class APIValidator:

    @staticmethod
    def validate_status_code(response, expected_status):
        assert response.status_code == expected_status, (
            f"Expected {expected_status}, "
            f"but got {response.status_code}"
        )

    @staticmethod
    def validate_json_response(response):
        assert "application/json" in response.headers.get(
            "Content-Type", ""
        )

    @staticmethod
    def validate_key(data, key):
        assert key in data, (
            f"Expected key '{key}' not found"
        )

    @staticmethod
    def validate_value(data, key, expected_value):
        assert data[key] == expected_value, (
            f"Expected {key}={expected_value}, "
            f"but got {data[key]}"
        )

    @staticmethod
    def validate_data_type(data, key, expected_type):
        assert isinstance(data[key], expected_type), (
            f"Expected {key} to be {expected_type.__name__}"
        )


def validate_required_fields(data, required_fields):
    for field in required_fields:
        assert field in data, (
            f"Required field '{field}' not found"
        )


def validate_field_value(data, field, expected_value):
    assert field in data, (
        f"Field '{field}' not found"
    )

    assert data[field] == expected_value, (
        f"Expected {field}={expected_value}, "
        f"but got {data[field]}"
    )
