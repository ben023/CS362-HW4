import unittest
import cube

class TestCube(unittest.TestCase):
    def test1(self):
        self.assertEqual(cube.cube(0), 0)
    def test2(self):
        self.assertEqual(cube.cube(2), 8)
    def test3(self):
        self.assertEqual(cube.cube("should fail"), "did not fail")

if __name__ == '__main__':
    unittest.main()