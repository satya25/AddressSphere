import pytest
from app.models import Address

@pytest.fixture
def address():
    return Address()

def test_get_all_addresses(address):
    addresses = address.get_all_addresses()
    assert isinstance(addresses, list)

def test_get_all_active_addresses(address):
    active_addresses = address.get_all_active_addresses()
    assert isinstance(active_addresses, list)

def test_get_all_deleted_addresses(address):
    deleted_addresses = address.get_all_deleted_addresses()
    assert isinstance(deleted_addresses, list)

def test_create_address(address):
    new_address_id = address.create_address("John Doe", "123 Main St", "Example City", "EX", "12345", "Example Country")
    assert new_address_id is not None

def test_update_address(address):
    # Debug: Print the current state of the address before update
    print("Before update:", address.get_address_by_id(1))

    # Update with different data
    rows_affected = address.update_address(1, "Jane Smith", "456 Elm St", "New City", "NY", "67890", "New Country")

    # Debug: Print the current state of the address after update
    print("After update:", address.get_address_by_id(1))

    assert rows_affected > 0

def test_delete_address(address):
    rows_affected = address.delete_address(1)
    assert rows_affected > 0

def test_restore_address(address):
    rows_affected = address.restore_address(1)
    assert rows_affected > 0
