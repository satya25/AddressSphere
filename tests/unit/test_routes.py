import os
import sys
import json
import pytest

# Add the root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_get_addresses(client):
    response = client.get('/api/addresses')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_active_addresses(client):
    response = client.get('/api/addresses/active')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_deleted_addresses(client):
    response = client.get('/api/addresses/deleted')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_address(client):
    new_address = {
        "name": "John Doe",
        "street": "123 Main St",
        "city": "Example City",
        "state": "EX",
        "zip_code": "12345",
        "country": "Example Country"
    }
    response = client.post('/api/addresses', data=json.dumps(new_address), content_type='application/json')
    assert response.status_code == 201
    assert response.json["message"] == "Address created"

def test_update_address(client):
    updated_address = {
        "name": "Jane Doe",
        "street": "123 Main St",
        "city": "Example City",
        "state": "EX",
        "zip_code": "12345",
        "country": "Example Country"
    }
    response = client.put('/api/addresses/1', data=json.dumps(updated_address), content_type='application/json')
    assert response.status_code == 200
    assert response.json["message"] == "Address updated"

def test_delete_address(client):
    response = client.delete('/api/addresses/1')
    assert response.status_code == 200
    assert response.json["message"] == "Address deleted"

def test_restore_address(client):
    response = client.put('/api/addresses/1/restore')
    assert response.status_code == 200
    assert response.json["message"] == "Address restored"

def test_get_total_records(client):
    response = client.get('/api/addresses/total')
    assert response.status_code == 200
    assert "total_records" in response.json

def test_get_total_active_records(client):
    response = client.get('/api/addresses/active/total')
    assert response.status_code == 200
    assert "total_active_records" in response.json

def test_get_total_deleted_records(client):
    response = client.get('/api/addresses/deleted/total')
    assert response.status_code == 200
    assert "total_deleted_records" in response.json
