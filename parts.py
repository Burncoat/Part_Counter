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

#GS Great Swords
HBI = Weapon(
    "Hope Blade I",
    gs,
    exp,
    200,
    1
    )

HBII = Weapon(
    "Hope Blade II",
    gs,
    exp,
    500,
    1,
    HBI,
    {"Iron Ore": 2}
)

HBIII = Weapon(
    "Hope Blade III",
    gs,
    exp,
    1500,
    3,
    HBII,
    {"Dragonite Ore": 3, "Machalite Ore": 2}
)

HBIV = Weapon(
    "Hope Blade IV",
    gs,
    exp,
    4000,
    5,
    HBIII,
    {"Carbalite Ore": 4}
)

HBV = Weapon(
    "Hope Blade V",
    gs,
    exp,
    14000,
    7,
    HBIV,
    {"Monster Hardbone": 4, "Fucium Ore": 5}
)

ESPB = Weapon(
    "Esperanza Blade",
    gs,
    exp,
    8,
    20000,
    HBV,
    {"Hunter Symbol 1": 5, "Bird Wyvern Gem": 1}
)

AWI = Weapon(
    "Albirath Wing I",
    gs,
    grath,
    2600,
    4,
    HBIII,
    {f"{grath} Scale": 3, f"{grath} Webbing": 2, "Flame Sac": 1}
)

AWII = Weapon(
    "Albirath Wing II",
    gs,
    grath,
    10000,
    6,
    AWI,
    {
        f"{grath} Certificate S": 2,
        f"{grath} Wing": 5,
        f"{grath} Plate": 1,
        "Guardian Blood+": 1
    }
)

WHR = Weapon(
    "Whitefire Rathguard",
    gs,
    grath,
    20000,
    8,
    AWII,
    {
        "Hunter Symbol II": 5,
        f"{grath} Carapace": 6,
        f"{grath} Ruby": 1,
        "Guardian Scale+": 6
    }
)

BSI = Weapon(
    "Buster Sword I",
    gs,
    ore,
    800,
    2,
    HBI,
    {"Machalite Ore": 1, "Earth Crystal": 2}
)

BSII = Weapon(
    "Buster Sword II",
    gs,
    ore,
    2600,
    4,
    BSI,
    {"Lightcrystal": 1, "Icium": 2}
)

BSIII = Weapon(
    "Buster Sword III",
    gs,
    ore,
    10000,
    6,
    BSII,
    {"Fucium Ore": 4, "Gracium": 3, "Monster Keenbone": 3}
)

RAV = Weapon(
    "Ravager Blade",
    gs,
    ore,
    20000,
    8,
    BSIII,
    {
        "Hunter Symbol I": 5,
        "Novacrystal": 1,
        "Wyvern Gem": 1
    }
)

JDI = Weapon(
    "Jin Dhavaar I",
    gs,
    jin,
    14000,
    7,
    BSIII,
    {
        f"{jin} Certificate S": 1,
        f"{jin} Claw+": 5,
        f"{jin} Iceplate": 4,
        f"{jin} Tail": 1
    }
)

PRM = Weapon(
    "Precipice Metallam",
    gs,
    jin,
    20000,
    8,
    JDI,
    {
        "Hunter Symbol III": 5,
        f"{jin} Horn": 4,
        f"{jin} Carapace": 4,
        f"{jin} Icegem": 1
    }
)

QEI = Weapon(
    f"{que} Espada II",
    gs,
    que,
    500,
    1,
    HBI,
    {f"{que} Scale": 3, f"{que} Igniter": 2, f"{que} Crest": 1}
)

QEII = Weapon(
    f"{que} Espada II",
    gs,
    que,
    1500,
    3,
    QEI,
    {"Firestone": 1, f"{que} Tail": 1, "Dragonite Ore": 1}
)

QEIII = Weapon(
    f"{que} Espada III",
    gs,
    que,
    4000,
    5,
    QEII,
    {
        f"{que} Certificate S": 2,
        f"{que} Igniter+": 5,
        f"{que} Crest+": 3
    }
)

QEIV = Weapon(
    f"{que} Espada IV",
    gs,
    que,
    14000,
    7,
    QEIII,
    {
        f"{nud} Certificate S": 3,
        f"{que} Hide+": 6,
        "Inferno Sac": 5,
        "Wyvern Gem": 1
    }
)

FIB = Weapon(
    "Firetail Blaisdell",
    gs,
    que,
    20000,
    8,
    QEIV,
    {
        "Hunter Symbol I": 5,
        f"{que} Scale+": 6,
        f"{nud} Flamegem": 1
    }
)

PBI = Weapon(
    "Paretic Blade I",
    gs,
    par,
    500,
    1,
    HBI,
    {f"{lal} Shell": 3, f"{lal} Mucus": 2, f"{lal} Claw": 1}
)

PBII = Weapon(
    "Paretic Blade II",
    gs,
    par,
    1500,
    3,
    PBI,
    {f"{ners} Claw": 1, f"{lal} Floret": 3, f"{lal} Stinger": 1}
)

PBIII = Weapon(
    "Paretic Blade III",
    gs,
    par,
    4000,
    5,
    PBII,
    {f"{lal} Certificate S": 2, f"{lal} Mucus+": 5, f"{lal} Claw+": 3}
)

PBIV = Weapon(
    "Paretic Blade IV",
    gs,
    par,
    14000,
    7,
    PBIII,
    {
        "Monster Hardbone": 3,
        f"{lal} Floret+": 6,
        f"{lal} Stinger+": 4
    }
)

DET = Weapon(
    "Destructive Torpor",
    gs,
    par,
    20000,
    8,
    PBIV,
    {
        "Hunter Symbol I": 5,
        f"{lal} Carapace": 6,
        "Monster Broth": 4,
        "Bird Wyvern Gem": 1
    }
)