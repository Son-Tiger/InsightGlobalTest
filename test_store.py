from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_
import random

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''

@pytest.fixture
def pet_data():
    payload = {
        "id": random.randint(1, 10),
        "name": "Solution Pet",
        "type": random.choice(["dog", "cat", "fish"]),
        "status": "available"
    }
    response = api_helpers.post_api_data("/pets/", payload)
    assert_that(response.status_code, is_(201))
    return response.json()


@pytest.fixture
def order_data(pet_data):
    payload = {
        "pet_id": pet_data["id"]
    }
    response = api_helpers.post_api_data("/store/order", payload)
    assert_that(response.status_code, is_(201))
    return response.json()


def test_patch_order_by_id(order_data):
    update_status = random.choice(["pending", "sold"])
    payload = {"status": update_status}
    response = api_helpers.patch_api_data(f"/store/order/{order_data['id']}", payload)
    assert_that(response.status_code, is_(200))
    assert_that(response.json()["message"], contains_string("Order and pet status updated successfully"))