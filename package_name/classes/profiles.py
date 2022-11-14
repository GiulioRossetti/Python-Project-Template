import json

__all__ = ["Profile", "Profiles"]


class Profile(object):

    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        """Return a string representation of the Profile object."""
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    def __dict__(self):
        """Return a dictionary representation of the Profile object."""
        return {"name": self.name, "age": self.age, "gender": self.gender}


class Profiles(object):
    def __init__(self):
        self.profiles = []

    def add_profile(self, profile: Profile):
        """Add a profile to the Profiles object."""
        self.profiles.append(profile)

    def __str__(self):
        """Return a string representation of the Profiles object."""
        return "".join([p.__str__() for p in self.profiles])

    def __dict__(self):
        """Return a dictionary representation of the Profiles object."""
        return {"profiles": [p.__dict__() for p in self.profiles]}

    def __eq__(self, other):
        """Return True if the Profiles objects are equal."""
        return self.__dict__() == other.__dict__()
