import httpx
import json

base_url = "http://192.168.0.89/json/state"


def get_infos():
    response = httpx.get(base_url).json()
    return json.dumps(response, indent=4)


def set_bri(bri_val: int = 144):
    request = httpx.post(
        base_url,
        json={"on": True, "bri": bri_val},
        headers={"Content-Type": "application/json"},
    )
    return request
