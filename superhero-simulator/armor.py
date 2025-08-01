import random

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)

# Optional testing code:
if __name__ == "__main__":
    shield = Armor("Shield", 30)
    print(shield.block())
