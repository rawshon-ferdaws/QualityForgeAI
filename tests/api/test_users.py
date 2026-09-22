from api.endpoints import Endpoints


# 1. GET single user
def test_get_user(api_client):

    response = api_client.get(
        Endpoints.user(1)
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert isinstance(data["name"], str)
    assert isinstance(data["email"], str)

    assert "application/json" in response.headers["Content-Type"]


# 2. GET all users - Collection Validation
def test_get_all_users(api_client):

    response = api_client.get(
        Endpoints.USERS
    )

    assert response.status_code == 200

    data = response.json()

    # Collection validation
    assert isinstance(data, list)
    assert len(data) > 0

    for user in data:
        assert "id" in user
        assert "name" in user
        assert "email" in user


# 3. GET users using Query Parameters
def test_get_user_with_query_parameter(api_client):

    response = api_client.get(
        Endpoints.USERS,
        params={"id": 1}
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["id"] == 1
