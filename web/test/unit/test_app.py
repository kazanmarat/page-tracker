# test/unit/test_app.py

import unittest.mock
from redis import ConnectionError

import pytest

from page_tracker.app import app

@pytest.fixture
def http_client():
    return app.test_client()

@unittest.mock.patch("page_tracker.app.redis")
def test_should_handle_redis_connection_error(mock_redis, http_client):
    # Given
    mock_redis.return_value.incr.side_effect = ConnectionError

    # When
    response = http_client.get("/")

    # Then
    assert response.status_code == 500
    assert response.text == "Sorry, something went wrong \N{pensive face}"
