from package_name.classes.profiles import *


def sort_profiles_by_age(profiles: Profiles) -> Profiles:
    """Sort the profiles by age."""
    profiles.profiles.sort(key=lambda x: x.age)
    return profiles


def sort_profiles_by_name(profiles: Profiles) -> Profiles:
    """Sort the profiles by name."""
    profiles.profiles.sort(key=lambda x: x.name)
    return profiles
