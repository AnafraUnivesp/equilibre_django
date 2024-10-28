"""
O django irá disponibilizar o objetivo Client para que possamos realizar o testes.
O objeto do tipo Client, irá emular requisições https.
Para isso realizo o import da classe e crio um get, o qual a respostá será obtida através da raiz do meu projeto
por isso inserimos ('/')

É necessario informar no settings.py a pasta onde os testes devem buscar as mensagens que foram requisitadas

from django.test import Client

def test_home_status_code(client:Client):
    resposta = client.get('/')
    assert resposta.status_code == 200


"""

import pytest
from django.urls import reverse
from django.test import Client

@pytest.fixture
def client():
    return Client()

def test_status_code(client):
    resposta = client.get(reverse('cadastro:home'))
    assert resposta.status_code == 200