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
def order_data():
    data = {
        "id": random.randint(1, 100),
        "petId": random.randint(1, 100),
        "status": "placed"
    }
    response = api_helpers.post_api_data("/store/order", data)
    assert_that(response.status_code, is_(200))
    return data

def test_patch_order_by_id(order_data):
    test_endpoint = "/store/order/{order_id}"
    response = api_helpers.get_api_data(test_endpoint)
    assert_that(response.status_code, is_(200))
    assert_that(response.json()["message"], contains_string("Order and pet status updated successfully"))
    validate(instance=response.json(), schema=schemas.order)