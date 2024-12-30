class Resource:
    def __init__(self, resource_type, amount):
        self.resource_type = resource_type
        self.amount = amount

    def collect(self, amount):
        if amount > self.amount:
            collected_amount = self.amount
            self.amount = 0
        else:
            collected_amount = amount
            self.amount -= amount
        return collected_amount

    def is_depleted(self):
        return self.amount <= 0
