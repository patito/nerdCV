# I wil tell you something I wrote the test after finishing my CV code.
# Yeah, I'm that crazy. I know I could test better, but it is just a CV and
# I promisse I will not merge with production branch or deploy in live, and
# I will create a check to monitor on Sensu and Prometheus.

# Run my test: python3 -m unittest -v -b test_cv.py

import unittest
from cv import PauloBenatto


class TestPauloBentto(unittest.TestCase):

    def setUp(self):
        self.plb = PauloBenatto()

    def test_battles(self):
        battles = self.plb.battles()
        self.assertEqual(len(battles), 5)
        self.assertEqual(battles["dba"]["warrior"],
                         "Software Engineer Freelancer")
        self.assertEqual(battles["return_of_brandwatch"]["weapons"],
                         ["linux", "golang", "rest apis"])
        self.assertEqual(len(list(filter(lambda x: x == "c",
                         battles["secplus"]["weapons"]))), 1)
        # Please, be equal 0, please
        self.assertEqual(len(list(filter(lambda x: x == "pascal",
                         battles["brandwatch"]["weapons"]))), 0)

    def test_weapons(self):
        weapons = self.plb.weapons()
        keys = weapons.keys()
        self.assertEqual(len(keys), 6)
        self.assertEqual("python" in keys, True)
        self.assertEqual("linux" in keys, True)
        # please be false _o/
        self.assertEqual("delphi" in keys, False)

    def test_contact(self):
        self.plb.contact()
        # Now you know my email =), but I'm still a douchebag
        import base64
        # converting bytes to str
        self.assertEqual(base64.b64decode(self.plb.email).decode("utf-8"),
                         "benatto@gmail.com")
        self.assertEqual(self.plb.blog, "http://benatto.xyz")
        self.assertEqual(self.plb.linkedin, "https://www.linkedin.com/in/benatto/")
        self.assertEqual(self.plb.github, "https://github.com/patito")

    def test_type(self):
        # please be true =)
        self.assertEqual(self.plb.type == "human", False)
        # please be false =(
        self.assertEqual(self.plb.type == "hobbit", True)

    def test_interest(self):
        self.assertEqual("surf" in self.plb.interests, False)
        self.assertEqual("guitar" in self.plb.interests, False)
        self.assertEqual("rock'n'roll" in self.plb.interests, False)
        # What is wrong with me, if you are reading that u know the
        # answer.
        self.assertEqual("coding" in self.plb.interests, True)
        self.assertEqual("linux" in self.plb.interests, True)


if __name__ == "__main__":
    unittest.main()
