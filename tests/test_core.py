import unittest
from core import filter_polymers

class TestPolymerCore(unittest.TestCase):

    def setUp(self):
        self.sample = [
            {"Name": "A", "MolecularWeight": 10000, "GlassTransitionTemp": 50, "Density": 1.0},
            {"Name": "B", "MolecularWeight": 20000, "GlassTransitionTemp": 100, "Density": 1.5},
            {"Name": "C", "MolecularWeight": 30000, "GlassTransitionTemp": 150, "Density": 2.0},
        ]

    def test_filter_by_mw(self):
        result = filter_polymers(self.sample, min_mw=15000, max_mw=25000)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["Name"], "B")

    def test_filter_by_tg(self):
        result = filter_polymers(self.sample, min_tg=90, max_tg=160)
        self.assertEqual(len(result), 2)

    def test_filter_by_density(self):
        result = filter_polymers(self.sample, min_density=1.4, max_density=2.1)
        self.assertEqual(len(result), 2)

    def test_combined_filter(self):
        result = filter_polymers(self.sample, min_mw=10000, max_mw=30000, min_density=1.4, max_density=2.1)
        self.assertEqual(len(result), 2)

if __name__ == "__main__":
    unittest.main()