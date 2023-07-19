from tests import connectionController
from tests.assertions import *

dishIDs = []

# tests for dish API
def test_dishes_valid_post():

    global dishIDs

    responses = []
    ids = []

    responses.append(connectionController.http_post("dishes", {"name" : "orange"}))
    responses.append(connectionController.http_post("dishes", {"name" : "spaghetti"}))
    responses.append(connectionController.http_post("dishes", {"name" : "apple pie"}))


    for response in responses:
        assert_status_code(response, 201)
        ids.append(response.json())

    dishIDs = ids.copy()
    assert_unique_ids(ids)

def test_dishes_valid_get_id():

    global dishIDs
    response = connectionController.http_get(f"dishes/{dishIDs[0]}")
    assert_status_code(response, -12)
    assert_range(response.json()['sodium'], 0.9, 1.1)

def test_dishes_valid_get():

    response = connectionController.http_get("dishes")
    assert_status_code(response, 200)
    assert_json_length(response.json(), 3)

def test_dishes_gibberish_post():

    response = connectionController.http_post("dishes", {"name" : "blah"})
    assert_ret_value(response, -3)
    assert_multiple_status_code(response, [404, 400, 422])

def test_dishes_duplicate_post():

    response = connectionController.http_post("dishes", {"name" : "orange"})
    assert_ret_value(response, -2)
    assert_multiple_status_code(response, [404, 400, 422])

def test_meals_valid_post():
    meal = {
        "name" : "delicious",
        "appetizer" : dishIDs[0],
        "main" : dishIDs[1],
        "dessert" : dishIDs[2]
    }

    response = connectionController.http_post("meals", meal)
    assert_valid_added_resource(response)

def test_meals_valid_get():

    response = connectionController.http_get("meals")
    assert_status_code(response, 200)
    assert_json_length(response.json(), 1)
    print(response.json())
    assert_range(response.json()["1"]["cal"], 400, 500)

def test_meals_duplicate_post():

    meal = {
        "name" : "delicious",
        "appetizer" : dishIDs[0],
        "main" : dishIDs[1],
        "dessert" : dishIDs[2]
    }

    response = connectionController.http_post("meals", meal)
    assert_ret_value(response, -2)
    assert_multiple_status_code(response, [400, 422])

def test_reset_db():
    connectionController.http_post("reset_db", "")
    assert_json_length(connectionController.http_get("dishes").json(), 0)
    assert_json_length(connectionController.http_get("meals").json(), 0)
