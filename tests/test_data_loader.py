import unittest
from engine.data_loader import DataLoader
import json
import os

class TestDataLoader(unittest.TestCase):

    def setUp(self):
        self.units_file = 'test_units.json'
        self.resources_file = 'test_resources.json'
        self.units_data = {
            "unit1": {"health": 100, "attack": 10},
            "unit2": {"health": 200, "attack": 20}
        }
        self.resources_data = {
            "wood": {"amount": 1000},
            "gold": {"amount": 500}
        }
        with open(self.units_file, 'w') as file:
            json.dump(self.units_data, file)
        with open(self.resources_file, 'w') as file:
            json.dump(self.resources_data, file)

    def tearDown(self):
        os.remove(self.units_file)
        os.remove(self.resources_file)

    def test_load_units(self):
        data_loader = DataLoader(self.units_file, self.resources_file)
        loaded_units = data_loader.load_units()
        self.assertEqual(loaded_units, self.units_data)

    def test_load_resources(self):
        data_loader = DataLoader(self.units_file, self.resources_file)
        loaded_resources = data_loader.load_resources()
        self.assertEqual(loaded_resources, self.resources_data)

if __name__ == '__main__':
    unittest.main()
