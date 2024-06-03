import unittest
from ggt import ggt

class test_ggt(unittest.TestCase):
    def test_types(self):
        self.assertRaises(TypeError, ggt, *(True, 0))
        self.assertRaises(TypeError, ggt, *(0, True))
        self.assertRaises(TypeError, ggt, *(3j, 0))
        self.assertRaises(TypeError, ggt, *(True, 3j))
        self.assertRaises(TypeError, ggt, *("Hund", 0))
        self.assertRaises(TypeError, ggt, *(0, "Hund"))

    def test_bad_values(self):
        self.assertRaises(ValueError, ggt, *(-44, -18))
        self.assertRaises(ValueError, ggt, *(-16, 23))
        self.assertRaises(ValueError, ggt, *(23, -16))
    
    def test_values(self):
        self.assertEqual(ggt(12, 18), 6)
        self.assertEqual(ggt(10, 20), 10)
        self.assertEqual(ggt(20, 10), 10)
        self.assertEqual(ggt(18, 12), 6)
        self.assertEqual(ggt(12, 15), 3)
        self.assertEqual(ggt(16, 60), 4)
        self.assertEqual(ggt(60, 16), 4)
        self.assertEqual(ggt(15, 60), 15)
        self.assertEqual(ggt(12, 60), 12)
        self.assertEqual(ggt(20, 30), 10)
        self.assertEqual(ggt(20, 60), 20)
        self.assertEqual(ggt(12, 60), 12)
        self.assertEqual(ggt(21, 130), 1)
        self.assertEqual(ggt(24, 60), 12)
        self.assertEqual(ggt(50, 100), 50)
        self.assertEqual(ggt(768, 912), 48)    

unittest.main()