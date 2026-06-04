from pokemon import get_pokemon
from unittest.mock import Mock
import requests

def test_pokemon_not_found(monkeypatch, capsys):

    # Fake API
    fake_response = Mock()
    fake_response.status_code = 404

    # Simular Request
    monkeypatch.setattr(requests, "get", lambda _: fake_response) #-> Poderia usar ("request.get")

    result = get_pokemon("none")

    # Pegar o print
    captura = capsys.readouterr()

    # Verifica se aparece a mensagem "Pokemon not found"
    assert result is None


def test_connection_error(monkeypatch, capsys):


    def mock_get(_):
        raise requests.exceptions.RequestException
    
    monkeypatch.setattr(requests, "get", mock_get)
    
    result = get_pokemon("pikachu")

    captura = capsys.readouterr()

    assert result is None