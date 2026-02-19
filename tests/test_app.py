from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_read_root():
    """
    Esse teste tem 3 etapas (AAA)
    A: Arrange (Organização)
    A: Act (Ação)
    A: Assert (Verificação)
    teardown (limpeza) - não tem nesse caso, mas é importante saber que existe 
    """
    # Arrange
    client = TestClient(app)
    # Act
    response = client.get('/')
    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!'}
