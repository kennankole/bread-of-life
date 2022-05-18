
from pydoc import cli
from urllib import response


def test_home_page(client):
    response = client.get('/')
    assert b"Hello, there" in response.data