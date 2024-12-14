import os

import pytest
from fastapi.testclient import TestClient

from webapp import app

# Instantiate the client
client = TestClient(app)
print(f" root={os.getcwd()}")


@pytest.mark.skipif(True, reason="test not ready yet, Skip for now!")
class Test_WebServer:
    def test_api_requests(self):
        # home page
        response = client.get("/")
        assert response.status_code == 200
        # ai page
        response = client.get("/ai")
        assert response.status_code == 200
        # get_node_list page
        response = client.get("/get_node_list")
        assert response.status_code == 200
        # sensors page
        response = client.get("/sensors")
        assert response.status_code == 200

    def test_database(self):
        # get routes page
        response = client.get("/get_routes/node1")
        assert response.status_code == 200
