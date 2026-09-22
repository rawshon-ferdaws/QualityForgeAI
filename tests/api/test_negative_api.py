def test_negative_api_example():
    response = {
        "status_code": 400,
        "message": "Bad Request"
    }

    assert response["status_code"] == 400
