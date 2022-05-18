import pytest
from project import create_app

@pytest.fixture()
def application():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    
    yield app
    
    
@pytest.fixture()
def client(application):
    return application.test_client()
