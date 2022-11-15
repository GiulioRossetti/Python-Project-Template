import unittest
from package_name import Profiles, Profile
from package_name.readwrite import *


class TestAlgorithms(unittest.TestCase):
    def test_io_profiles(self):
        pls = Profiles()
        pls.add_profile(Profile("John", 20, "M"))
        pls.add_profile(Profile("Jane", 25, "F"))
        pls.add_profile(Profile("Jack", 22, "M"))
        pls.add_profile(Profile("Jill", 21, "F"))
        pls.add_profile(Profile("Jenny", 23, "F"))
        pls.add_profile(Profile("Jared", 24, "M"))

        json_str = to_json(pls)
        pls2 = from_json(json_str)
        self.assertEqual(pls, pls2)


if __name__ == "__main__":
    unittest.main()
