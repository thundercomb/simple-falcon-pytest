from falcon import testing, HTTP_200, HTTP_404
import pytest
import os
import requests

import app

@pytest.fixture()
def client():
    return testing.TestClient(app.create())

def test_get_message(client, mocker):
    doc = {u'message': u'Hello world!'}

    # Arrange
    get_mock = mocker.MagicMock()
    get_mock.json.return_value = doc
    get_mock.status_code = 200
    request_mock = mocker.patch.object(
        app.requests,
        'get',
        return_value=get_mock,
    )

    # Act
    response = client.simulate_get('/messages/1')

    # Assert
    typicode = response.json
    assert response.status == HTTP_200
    assert typicode == doc

def test_wrong_endpoint(client, mocker):
    doc = {u'message': u'Hello world!'}

    # Arrange
    get_mock = mocker.MagicMock()
    get_mock.json.return_value = doc
    get_mock.status_code = 200
    request_mock = mocker.patch.object(
        app.requests,
        'get',
        return_value=get_mock,
    )

    # Act
    response = client.simulate_get('/wrong/123')

    # Assert
    typicode = response.json
    assert response.status == HTTP_404
    assert typicode == None
