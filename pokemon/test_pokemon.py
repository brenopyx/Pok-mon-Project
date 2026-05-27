from pokemon import pokemon
from unittest.mock import Mock
import requests

def test_pokemon_not_found(monkeypatch, capsys):
    #Simular Input
    monkeypatch.setattr("builtins.input", lambda _: "algo") #-> Poderia usar (builtins, "input") mas teria que importar "builtins"

    #fake API
    fake_response = Mock()
    fake_response.status_code = 404

    #Simular Request
    monkeypatch.setattr(requests, "get", lambda _: fake_response) #-> Poderia usar ("request.get")

    pokemon()

    #Pegar o print
    captura = capsys.readouterr()

    #Verifica se aparece a mensagem "Pokemon not found"
    assert "Pokemon not found" in captura.out


def test_connection_error(monkeypatch, capsys):

    monkeypatch.setattr("builtins.input", lambda _: "pikachu")

    def mock_get(_):
        raise requests.exceptions.RequestException
    
    monkeypatch.setattr(requests, "get", mock_get)
    
    pokemon()

    captura = capsys.readouterr()

    assert "The server could be not acessed" in captura.out