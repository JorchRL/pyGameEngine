import json

class DataLoader:
    def __init__(self, units_file, resources_file):
        self.units_file = units_file
        self.resources_file = resources_file

    def load_units(self):
        with open(self.units_file, 'r') as file:
            units_data = json.load(file)
        return units_data

    def load_resources(self):
        with open(self.resources_file, 'r') as file:
            resources_data = json.load(file)
        return resources_data
