import os
from dotenv import load_dotenv, find_dotenv
import pytest
import requests
from todo_app import app

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

def full_url(path):
    trello_api_root = "https://api.trello.com/1"
    trello_api_key = os.getenv('TRELLO_API_KEY')
    trello_api_token = os.getenv('TRELLO_API_TOKEN')
    return f"{trello_api_root}{path}?key={trello_api_key}&token={trello_api_token}"

def stub(url, params = {}):
    test_board_id = os.environ.get("BOARD_ID")
    fake_response = None
    cards_path = f"/boards/{test_board_id}/cards"
    if url == full_url(cards_path):
        fake_response = [
            {
              "id": "card_1",
              "name": "Done job",
              "labels": [
                  {
                    "id": "label_1",
                    "name": "Complete",
                  }
              ],
            }
        ]
        return StubResponse(fake_response)

    raise Exception(f'Integration test did not expect URL "{url}"')

def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'get', stub)

    response = client.get('/')

    assert response.status_code == 200
    assert 'Done job' in response.data.decode()
