import unittest
from package_sorter import sort

class TestPackageSorter(unittest.TestCase):
    def test_standard_package(self):
        # Small, light package
        self.assertEqual(sort(10, 10, 10, 1), "STANDARD")
        # Just under all thresholds
        self.assertEqual(sort(100, 100, 99, 19), "STANDARD")

    def test_bulky_package(self):
        # Large volume but not heavy
        self.assertEqual(sort(100, 100, 100, 1), "SPECIAL")
        # One dimension over 150cm
        self.assertEqual(sort(151, 20, 20, 1), "SPECIAL")

    def test_heavy_package(self):
        # Heavy but small
        self.assertEqual(sort(10, 10, 10, 25), "SPECIAL")

    def test_rejected_package(self):
        # Both bulky and heavy
        self.assertEqual(sort(150, 150, 150, 25), "REJECTED")
        # One dimension over 150cm and heavy
        self.assertEqual(sort(151, 20, 20, 20), "REJECTED")

    def test_edge_cases(self):
        # Exactly at volume threshold
        self.assertEqual(sort(100, 100, 100, 1), "SPECIAL")  # 1,000,000 cm³
        # Exactly at mass threshold
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")
        # Exactly at dimension threshold
        self.assertEqual(sort(150, 10, 10, 1), "SPECIAL")

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            sort(-1, 10, 10, 10)
        with self.assertRaises(ValueError):
            sort(10, -1, 10, 10)
        with self.assertRaises(ValueError):
            sort(10, 10, -1, 10)
        with self.assertRaises(ValueError):
            sort(10, 10, 10, -1)
        with self.assertRaises(ValueError):
            sort(0, 10, 10, 10)

if __name__ == '__main__':
    unittest.main()
