import json
from pathlib import Path

from jsonschema import validate

from api.endpoints import Endpoints
from api.validators import APIValidator
from utilities.data_reader import DataReader


payloads = DataReader.load_json(
    "api_payloads.json"
)


# 1. GET - Verify single user
def test_get_user(api_client):

    response = api_client.get(
        Endpoints.user(1)
    )

    APIValidator.validate_status_code(
        response, 200
    )

    APIValidator.validate_json_response(
        response
    )

    data = response.json()

    APIValidator.validate_key(
        data, "id"
    )

    APIValidator.validate_value(
        data, "id", 1
    )

    APIValidator.validate_key(
        data, "name"
    )

    APIValidator.validate_key(
        data, "email"
    )

    APIValidator.validate_data_type(
        data, "id", int
    )


# 2. GET - Verify users collection
def test_get_users(api_client):

    response = api_client.get(
        Endpoints.USERS
    )

    APIValidator.validate_status_code(
        response, 200
    )

    APIValidator.validate_json_response(
        response
    )

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


# 3. GET - Query parameter validation
def test_get_posts_by_user(api_client):

    response = api_client.get(
        Endpoints.POSTS,
        params={"userId": 1}
    )

    APIValidator.validate_status_code(
        response, 200
    )

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    for post in data:
        assert post["userId"] == 1


# 4. POST - Create post
def test_create_post(api_client):

    payload = payloads["create_post"]

    response = api_client.post(
        Endpoints.POSTS,
        payload
    )

    APIValidator.validate_status_code(
        response, 201
    )

    APIValidator.validate_json_response(
        response
    )

    data = response.json()

    APIValidator.validate_value(
        data, "title", payload["title"]
    )

    APIValidator.validate_value(
        data, "body", payload["body"]
    )

    APIValidator.validate_value(
        data, "userId", payload["userId"]
    )

    APIValidator.validate_key(
        data, "id"
    )


# 5. PUT - Update complete post
def test_update_post(api_client):

    payload = payloads["update_post"]

    response = api_client.put(
        Endpoints.post(1),
        payload
    )

    APIValidator.validate_status_code(
        response, 200
    )

    data = response.json()

    APIValidator.validate_value(
        data, "title", payload["title"]
    )

    APIValidator.validate_value(
        data, "body", payload["body"]
    )

    APIValidator.validate_value(
        data, "userId", payload["userId"]
    )


# 6. PATCH - Partially update post
def test_patch_post(api_client):

    payload = payloads["patch_post"]

    response = api_client.patch(
        Endpoints.post(1),
        payload
    )

    APIValidator.validate_status_code(
        response, 200
    )

    data = response.json()

    APIValidator.validate_value(
        data, "title", payload["title"]
    )


# 7. DELETE - Delete post
def test_delete_post(api_client):

    response = api_client.delete(
        Endpoints.post(1)
    )

    APIValidator.validate_status_code(
        response, 200
    )


# 8. NEGATIVE - User does not exist
def test_get_nonexistent_user(api_client):

    response = api_client.get(
        Endpoints.user(999999)
    )

    APIValidator.validate_status_code(
        response, 404
    )


# 9. NEGATIVE - Post does not exist
def test_get_nonexistent_post(api_client):

    response = api_client.get(
        Endpoints.post(999999)
    )

    APIValidator.validate_status_code(
        response, 404
    )


# 10. RESPONSE SCHEMA - Validate user structure
def test_user_response_schema(api_client):

    response = api_client.get(
        Endpoints.user(1)
    )

    APIValidator.validate_status_code(
        response, 200
    )

    data = response.json()

    required_keys = [
        "id",
        "name",
        "username",
        "email",
        "address",
        "phone",
        "website",
        "company"
    ]

    for key in required_keys:
        APIValidator.validate_key(
            data, key
        )

    APIValidator.validate_data_type(
        data, "id", int
    )

    APIValidator.validate_data_type(
        data, "name", str
    )

    APIValidator.validate_data_type(
        data, "email", str
    )


# 11. JSON SCHEMA - Validate user API contract
def test_user_json_schema(api_client):

    response = api_client.get(
        Endpoints.user(1)
    )

    APIValidator.validate_status_code(
        response, 200
    )

    data = response.json()

    schema_path = (
        Path(__file__).resolve().parents[2]
        / "schemas"
        / "user_schema.json"
    )

    with open(
        schema_path,
        "r",
        encoding="utf-8"
    ) as file:
        schema = json.load(file)

    validate(
        instance=data,
        schema=schema
    )
