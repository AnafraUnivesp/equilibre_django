from django.urls import reverse


def test_status_code(client):
    resposta = client.get(reverse('cadastro:home'))
    assert resposta.status_code == 200