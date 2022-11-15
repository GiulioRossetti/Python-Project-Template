import json
from package_name.classes.profiles import *

__all__ = ["to_json", "from_json"]


def to_json(profiles: Profiles) -> str:
    """
    Convert the Profiles object to JSON.

    :param profiles: The Profiles object to convert.
    :return: The JSON string.

    :Example:

    >>> from package_name import Profiles, Profile
    >>> from package_name.readwrite import *
    >>> pls = Profiles()
    >>> pls.add_profile(Profile("John", 20, "M"))
    >>> pls.add_profile(Profile("Jane", 25, "F"))
    >>> pls.add_profile(Profile("Jack", 22, "M"))
    >>> pls.add_profile(Profile("Jill", 21, "F"))
    >>> pls.add_profile(Profile("Jenny", 23, "F"))
    >>> pls.add_profile(Profile("Jared", 24, "M"))
    >>> json_str = to_json(pls)

    """
    return json.dumps(profiles.__dict__())


def from_json(json_str: str) -> Profiles:
    """
    Convert the JSON string to a Profiles object.

    :param json_str: The JSON string to convert.
    :return: The Profiles object.

    :Example:

    >>> from package_name import Profiles, Profile
    >>> from package_name.readwrite import *
    >>> pls = Profiles()
    >>> pls.add_profile(Profile("John", 20, "M"))
    >>> pls.add_profile(Profile("Jane", 25, "F"))
    >>> pls.add_profile(Profile("Jack", 22, "M"))
    >>> pls.add_profile(Profile("Jill", 21, "F"))
    >>> pls.add_profile(Profile("Jenny", 23, "F"))
    >>> pls.add_profile(Profile("Jared", 24, "M"))
    >>> json_str = to_json(pls)
    >>> pls2 = from_json(json_str)
    """
    profiles = json.loads(json_str)
    pls = Profiles()
    for p in profiles["profiles"]:
        pls.add_profile(Profile(p["name"], p["age"], p["gender"]))
    return pls
