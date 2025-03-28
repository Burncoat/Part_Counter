from abbreviations import *

class Weapon():
    def __init__(
            self,
            name,
            type,
            tree,
            cost,
            rarity,
            parent = None,
            materials = None
        ):
        self.name = name
        self.type = type
        self.tree = f"{tree} Tree"
        self.cost = cost
        self.rarity = rarity
        self.parent = parent
        self.materials = materials
        
    def __repr__(self):
        if self.materials is None:
            return f"{self.name}, {self.type}, Rarity {self.rarity}, Tree: {self.tree}, Costs: {self.cost}z"
        mtr_string = ""
        for key, value in self.materials.items():
            mtr_string += f"{key} x{value}, "
        return f"{self.name}, {self.type}, Rarity {self.rarity}, Tree: {self.tree}, Costs: {mtr_string}{self.cost}z"

hope_blade_1 = Weapon(
    "Hope Blade I",
    gs,
    exp,
    200,
    1
    )
