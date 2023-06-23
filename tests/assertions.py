import requests
from typing import Union

def assert_unique_ids(ids: list[int]):
    assert len(set(ids)) == len(ids)

def assert_status_code(response: requests.Response, expected_status_code: int):
    assert response.status_code == expected_status_code

def assert_range(value: Union[float, int], min_value: Union[float, int], max_value: Union[float, int]):
    assert value >= min_value
    assert value <= max_value

def assert_json_length(json: dict, length: int):
    assert len(json) == length

def assert_multiple_status_code(response: requests.Response, expected_status_codes: list[int]):
    assert response.status_code in expected_status_codes

def assert_ret_value(response: requests.Response, returned_value: any):
    assert response.json() == returned_value

def assert_valid_added_resource(response: requests.Response):
    assert response.status_code == 201
    # should be positive ID
    VALID_RETURNED_RESOURCE_ID = 0
    assert response.json() > VALID_RETURNED_RESOURCE_ID




