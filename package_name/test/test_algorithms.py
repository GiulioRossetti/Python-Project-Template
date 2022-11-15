import unittest
from package_name.algorithms.sorting import *
from package_name.classes.profiles import *


class TestAlgorithms(unittest.TestCase):
    def test_sort_profiles(self):
        pls = Profiles()
        pls.add_profile(Profile("John", 20, "M"))
        pls.add_profile(Profile("Jane", 25, "F"))
        pls.add_profile(Profile("Jack", 22, "M"))
        pls.add_profile(Profile("Jill", 21, "F"))
        pls.add_profile(Profile("Jenny", 23, "F"))
        pls.add_profile(Profile("Jared", 24, "M"))

        age_sorted = sort_profiles_by_age(pls)
        self.assertEqual(age_sorted.profiles[0].name, "John")

        name_sorted = sort_profiles_by_name(pls)
        self.assertEqual(name_sorted.profiles[0].name, "Jack")


if __name__ == "__main__":
    unittest.main()
