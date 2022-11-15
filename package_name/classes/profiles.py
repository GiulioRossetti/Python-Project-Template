__all__ = ["Profile", "Profiles"]


class Profile(object):
    def __init__(self, name: str, age: int, gender: str):
        """
        Initialize the Profile object.

        :param name: The name of the profile.
        :param age: The age of the profile.
        :param gender: The gender of the profile.
        """
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        """
        Return a string representation of the Profile object.
        """
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    def __dict__(self):
        """
        Return a dictionary representation of the Profile object.
        """
        return {"name": self.name, "age": self.age, "gender": self.gender}


class Profiles(object):
    def __init__(self):
        """
        Initialize the Profiles object.
        """
        self.profiles = []

    def add_profile(self, profile: Profile):
        """
        Add a profile to the Profiles object.

        :param profile: The Profile object to add.

        """
        self.profiles.append(profile)

    def __str__(self):
        """
        Return a string representation of the Profiles object.
        """
        return "".join([p.__str__() for p in self.profiles])

    def __dict__(self):
        """
        Return a dictionary representation of the Profiles object.
        """
        return {"profiles": [p.__dict__() for p in self.profiles]}

    def __eq__(self, other):
        """
        Return True if the Profiles objects are equal.

        :param other: The other Profiles object to compare.
        """
        return self.__dict__() == other.__dict__()
