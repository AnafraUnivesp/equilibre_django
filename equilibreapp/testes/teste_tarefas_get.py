import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

@pytest.fixture
def resposta(client):
    resp = client.get(reverse('cadastro:home'))
    return resp

def test_status_code(resposta):
    assert resposta.status_code == 200

