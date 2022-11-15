from package_name.classes.profiles import *


def sort_profiles_by_age(profiles: Profiles) -> Profiles:
    """
    Sort the profiles by age.

    :param profiles: The Profiles object to sort.
    :return: The sorted Profiles object.

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
    >>> age_sorted = sort_profiles_by_age(pls)
    """
    profiles.profiles.sort(key=lambda x: x.age)
    return profiles


def sort_profiles_by_name(profiles: Profiles) -> Profiles:
    """
    Sort the profiles by name.

    :param profiles: The Profiles object to sort.
    :return: The sorted Profiles object.

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
    >>> age_sorted = sort_profiles_by_name(pls)
    """
    profiles.profiles.sort(key=lambda x: x.name)
    return profiles
