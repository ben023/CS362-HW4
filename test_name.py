import unittest
import name

class TestAverage(unittest.TestCase):
    def test1(self):
        self.assertEqual(name.full_name("Bob","Smith"), "Bob Smith")
    def test2(self):
        self.assertEqual(name.full_name("Fail1","Fail2"), "Invalid name")
    def test3(self):
        self.assertEqual(name.full_name("Luke","Skywalker"), "Luke Skywalker")

if __name__ == '__main__':
    unittest.main()