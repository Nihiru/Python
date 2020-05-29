import pytest
import requests
import json


@pytest.mark.parametrize("userid, firstname", [(1, "George"), (2, "Janet")])
def test_list_valid_user(supply_url, userid, firstname):
    url = supply_url + "/users/" + str(userid)
    resp = requests.get(url)
    j = json.loads(resp.text)
    assert resp.status_code == 200
    assert j["data"]["id"] == userid
    assert j["data"]["firstname"] == firstname


def test_list_invalid_user(supply_url):
    url = supply_url + "/users/50"
    resp = requests.get(url)
    assert resp.status_code == 404
