from http import HTTPStatus

from fastapi_zero.schemas import UserPublic
from fastapi_zero.security import create_access_token


# Generic
def test_read_root(client):
    """
    Esse teste tem 3 etapas (AAA)
    A: Arrange (Organização)
    A: Act (Ação)
    A: Assert (Verificação)
    teardown (limpeza) - não tem nesse caso, mas é importante saber que existe
    """
    # Arrange
    # client = TestClient(app)  (DNY -> CONFTEST.PY)
    # Act
    response = client.get('/')
    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_html_response(client):

    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <h1> Olá mundo!</h1>
    """
    )