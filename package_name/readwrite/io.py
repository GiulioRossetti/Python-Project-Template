import json
from package_name.classes.profiles import *


def to_json(profiles: Profiles) -> str:
    """Convert the Profiles object to JSON."""
    return json.dumps(profiles.__dict__())


def from_json(json_str: str) -> Profiles:
    """Convert the JSON string to a Profiles object."""
    profiles = json.loads(json_str)
    pls = Profiles()
    for p in profiles["profiles"]:
        pls.add_profile(Profile(p["name"], p["age"], p["gender"]))
    return pls
