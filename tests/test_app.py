from http import HTTPStatus

from fastapi.responses import Response
from fastapi.testclient import TestClient

from fastapi_boaspraticas.app import app


def test_root_deve_retornar_ola_fernanda():
    """Esse teste tem 3 etapas (AAA)
    - A = Arrange - Arranjo/Organizar da coisa
    - A: Act      - Executa/Agir a coisa (o SUT)
    - A: Assert   - Garanta/Afirmar que X e X
    """

    # Arrange
    client = TestClient(app)

    # Act
    response: Response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Ola, Fernanda!'}
    assert response.status_code == HTTPStatus.OK
