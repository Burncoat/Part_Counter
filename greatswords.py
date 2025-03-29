from abbreviations import *
from item import Weapon

#Expedition Tree
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
    {"Hunter Symbol I": 5, "Bird Wyvern Gem": 1}
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

#Bone Tree
BBI = Weapon(
    "Bone Blade I",
    gs,
    bone,
    500,
    1,
    None,
    {"Mystery Bone": 2}
)

BBII = Weapon(
    "Bone Blade II",
    gs,
    bone,
    800,
    2,
    BBI,
    {"Sturdy Bone": 2, "Monster Fluid": 1}
)

BBIII = Weapon(
    "Bone Blade III",
    gs,
    bone,
    2600,
    4,
    BBII,
    {"Tough Guardian Bone": 2}
)

BBIV = Weapon(
    "Bone Blade IV",
    gs,
    bone,
    10000,
    6,
    BBIII,
    {"Great Stoutbone": 4, "Colossal Bone": 2}
)

BOS = Weapon(
    "Bone Slasher",
    gs,
    bone,
    20000,
    8,
    BBIV,
    {
        "Hunter Symbol I": 5,
        "Monster Hardbone": 5,
        "Dragonbone Relic": 1,
        "Beast Gem": 1
    }
)

NKI = Weapon(
    "Nu Krake I",
    gs,
    nud,
    2600,
    4,
    BBII,
    {
        f"{nud} Hide": 3,
        f"{nud} Spike": 2,
        f"{nud} Oilmucus": 1
    }
)

NKII = Weapon(
    "Nu Krake II",
    gs,
    nud,
    14000,
    7,
    NKI,
    {
        f"{nud} Certificate S": 3,
        f"{nud} Spike+": 5,
        f"{nud} Oilmucus+": 4,
        f"{nud} Cerebrospinal Fluid": 1
    }
)

ABK = Weapon(
    "Abaddonian Krake",
    gs,
    nud,
    20000,
    8,
    NKII,
    {
        "Hunter Symbol III": 5,
        f"{nud} Tentacle+": 6,
        f"{nud} Horn+": 4,
        f"{nud} Flamegem": 1
    }
)

IBI = Weapon(
    "Immane Blade I",
    gs,
    ners,
    1500,
    3,
    BBII,
    {
        f"{ners} Shell": 3,
        f"{ners} Claw": 2,
        "Sleep Sac": 1
    }
)

IBII = Weapon(
    "Immane Blade II",
    gs,
    ners,
    5000,
    5,
    IBI,
    {
        f"{ners} Certificate S": 2,
        f"{ners} Claw+": 6,
        "Coma Sac": 6
    }
)

IBIII = Weapon(
    "Immane Blade III",
    gs,
    ners,
    14000,
    7,
    IBII,
    {
        f"{jin} Certificate S": 3,
        f"{ners} Spike+": 5,
        f"{ners} Shear": 2,
        "Monster Broth": 3
    }
)

IMB = Weapon(
    "Immolator Blade",
    gs,
    ners,
    20000,
    8,
    IBIII,
    {
        "Hunter Symbol I": 5,
        f"{ners} Carapace": 6,
        "Bird Wyvern Gem": 1
    }
)

NGSI = Weapon(
    "Nihil Great Sword I",
    gs,
    xwu,
    2600,
    4,
    IBI,
    {
        f"{xwu} Hide": 3,
        f"{xwu} Claw": 2,
        f"{xwu} Fang": 1
    }
)

NGSII = Weapon(
    "Nihil Great Sword II",
    gs,
    xwu,
    10000,
    6,
    NGSI,
    {
        f"{xwu} Certificate S": 2,
        f"{xwu} Claw+": 6,
        f"{xwu} Fang+": 4,
        f"{xwu} Cerebrospinal Fluid": 1
    }
)

PRD = Weapon(
    "Prinvrilo's Dissolution",
    gs,
    xwu,
    20000,
    8,
    NGSII,
    {
        "Hunter Symbol II": 5,
        "Golden Corneum+": 6,
        f"{xwu} Tentacle+": 4,
        f"{xwu} Umbragem": 1
    }

)

DFI = Weapon(
    "Dosha Fellslayer I",
    gs,
    dos,
    800,
    2,
    BBI,
    {
        f"{dos} Fur": 3,
        f"{dos} Claw": 2,
        f"{dos} Fang": 1
    }
)

DFII = Weapon(
    "Dosha Fellslayer II",
    gs,
    dos,
    2600,
    4,
    DFI,
    {
        f"{gdos} Claw": 1,
        f"{dos} Hide": 3,
        "Tough Guardian Bones": 1
    }
)

DFIII = Weapon(
    "Dosha Fellslayer III",
    gs,
    dos,
    10000,
    6,
    DFII,
    {
        f"{dos} Certificate S": 2,
        f"{dos} Claw+": 6,
        f"{dos} Fang+": 4
    }
)

FED = Weapon(
    "Fellslayer Dangeom",
    gs,
    dos,
    20000,
    8,
    DFIII,
    {
        "Hunter Symbol II": 5,
        f"{dos} Hide+": 6,
        "Beast Gem": 1
    }
)

GVGI = Weapon(
    "G Veldian Gladius I",
    gs,
    gark,
    2600,
    4,
    DFI,
    {
        "Guardian Scale": 3,
        "Guardian Pelt": 3,
        "Guardian Blood": 1,
        "Tough Guardian Bone": 2
    }
)

GVGII = Weapon(
    "G Veldian Gladius II",
    gs,
    gark,
    10000,
    6,
    GVGI,
    {
        "Guardian Scale+": 6,
        "Guardian Pelt+": 6,
        "Guardian Blood+": 3,
        "Dragonbone Relic": 1
    }
)

GSL = Weapon(
    "G Stalwart Lamorak",
    gs,
    gark,
    20000,
    8,
    GVGII,
    {
        "Hunter Symbol III": 5,
        f"{ark} Calloushell": 4,
        f"{ark} Tail": 2,
        f"{ark} Gem": 1
    }
)

VGI = Weapon(
    "Veldian Gladius I",
    gs,
    ark,
    14000,
    7,
    GVGII,
    {
        f"{ark} Certificate S": 3,
        f"{ark} Scale+": 4,
        f"White {ark} Pelt": 2,
        "Wyvern Gem": 1
    }
)

STL = Weapon(
    "Stalwart Lamorak",
    gs,
    ark,
    20000,
    8,
    VGI,
    {
        "Hunter Symbol III": 5,
        f"{ark} Armorplate": 5,
        f"{ark} Horn+": 3,
        f"{ark} Gem": 1
    }
)

DGI = Weapon(
    "Dosha Grimslayer I",
    gs,
    gdos,
    2600,
    4,
    DFI,
    {
        f"{gdos} Fur": 3,
        f"{gdos} Claw": 2,
        f"{gdos} Fang": 1
    }
)

DGII = Weapon(
    "Dosha Grimslayer II",
    gs,
    gdos,
    10000,
    6,
    DGI,
    {
        f"{gdos} Certificate S": 2,
        f"{gdos} Claw+": 6,
        f"{gdos} Fang+": 4,
        "Guardian Blood+": 1
    }
)

GRU = Weapon(
    "Grimslayer Urgeom",
    gs,
    gdos,
    20000,
    8,
    DGII,
    {
        "Hunter Symbol II": 5,
        f"{gdos} Fur+": 6,
        f"{gdos} Pelt+": 6,
        "Beast Gem": 1
    }
)

#Independent Trees
CDI = Weapon(
    "Chicken Decapitator I",
    gs,
    ykk,
    4000,
    5,
    None,
    {
        f"{ykk} Certificate S": 1,
        f"{ykk} Wing": 3,
        f"{ykk} Ear": 2,
        f"{ykk} Scale+": 5
    }
)

CDII = Weapon(
    "Chicken Decapitator II",
    gs,
    ykk,
    14000,
    7,
    CDI,
    {
        f"{nud} Certificate S": 2,
        "Giant Beak": 4,
        "Inferno Sack": 4
    }
)

ROD = Weapon(
    "Rooster Decapitator",
    gs,
    ykk,
    20000,
    8,
    CDII,
    {
        "Hunter Symbol I": 5,
        f"{ykk} Carapace": 6,
        f"{nud} Flamegem": 1
    }
)

SFI = Weapon(
    "Smiting Fulgur I",
    gs,
    gful,
    10000,
    6,
    CDI,
    {
        f"{gful} Certificate S": 2,
        f"{gful} Fang+": 5,
        f"{gful} Tail": 1,
        "Thunder Sac": 4
    }
)

FUG = Weapon(
    "Fulgurcleaver Guardiana",
    gs,
    gful,
    20000,
    8,
    SFI,
    {
        "Hunter Symbol II": 5,
        f"{gful} Nosebone+": 4,
        f"{gful} Pelt+": 6,
        f"{gful} Gem": 1
    }
)

SLI = Weapon(
    "Slaughter I",
    gs,
    gyp,
    4000,
    5,
    None,
    {
        f"{gyp} Certificate S": 1,
        f"{gyp} Wing": 3,
        f"{gyp} Head": 2,
        "Rubbery Hide+": 5
    }
)

SLII = Weapon(
    "Slaughter II",
    gs,
    gyp,
    10000,
    6,
    SLI,
    {
        f"{grav} Certificate S": 2,
        f"{gyp} Tail": 4,
        "Toxin Sac": 4
    }
)

POK = Weapon(
    "Poison King",
    gs,
    gyp,
    20000,
    8,
    SLII,
    {
        "Hunter Symbol I": 5,
        "Rubbery Hide+": 6,
        "Byrd Wyvern Gem": 1,
        "Novacrystal": 1
    }
)

VBI = Weapon(
    "Valkyrie Blade I",
    gs,
    rat,
    5000,
    5,
    None,
    {
        f"{rat} Certificate S": 1,
        f"{rat} Webbing": 3,
        f"{rat} Spike+": 2,
        f"{rat} Scale+": 5
    }
)

VBII = Weapon(
    "Valkyrie Blade II",
    gs,
    rat,
    14000,
    7,
    VBI,
    {
        f"{rey} Certificate S": 2,
        f"{rat} Carapace": 6,
        "Rath Medulla": 1,
        "Wyvern Gem": 1
    }
)

SIEG = Weapon(
    "Sieglinde",
    gs,
    rat,
    20000,
    8,
    VBII,
    {
        "Hunter Symbol I": 5,
        f"{rat} Scale+": 5,
        f"{rat} Ruby": 1
    }
)

RWI = Weapon(
    "Red Wing I",
    gs,
    rath,
    10000,
    6,
    VBI,
    {
        f"{rath} Certificate S": 2,
        f"{rath} Carapace": 5,
        f"{rath} Wing": 4,
        "Rath Medulla": 1
    }
)

RAF = Weapon(
    "Rathalos Firesword",
    gs,
    rath,
    20000,
    8,
    RWI,
    {
        "Hunter Symbol II": 5,
        f"{rath} Scale+": 6,
        f"{rath} Tail": 1,
        f"{rath} Ruby": 1
    }
)

SCHTNI = Weapon(
    "Schattenstolz I",
    gs,
    gor,
    14000,
    7,
    RWI,
    {
        f"{gor} Certificate S": 3,
        f"{gor} Riplaw+": 4,
        f"{gor} Tail": 1,
        "Frenzy Shard": 5
    }
)

DUS = Weapon(
    "Dusterstolz",
    gs,
    gor,
    20000,
    8,
    SCHTNI,
    {
        "Hunter Symbol III": 5,
        f"{gor} Feeler+": 2,
        f"{gor} Nyctgem": 1,
        "Frenzy Crystal": 5
    }
)

FSI = Weapon(
    "Frozen Speartuna I",
    gs,
    tuna,
    2600,
    4,
    None,
    {
        f"{tuna} Fin": 1,
        "Frozen Icebone": 5,
        "Frost Sac": 5
    }
)

FSII = Weapon(
    "Frozen Speartuna II",
    gs,
    tuna,
    10000,
    6,
    FSI,
    {
        "Great Stoutbone": 5,
        "Gracium": 5,
        "Freezer Sac": 4,
        f"{tuna} Fin": 2
    }
)

FRS = Weapon(
    "Freezer Speartuna",
    gs,
    tuna,
    20000,
    8,
    FSII,
    {
        "Hunter Symbol I": 5,
        "Dragonbone Relic": 1,
        f"{jin} Icegem": 1,
        f"{tuna} Fin": 3
    }
)

JBI = Weapon(
    "Jawblade I",
    gs,
    wrk,
    10000,
    6,
    None,
    {
        "Commission Ticket": 1,
        "Monster Keenbone": 5,
        "Stoutbone": 5,
        "Quality Bone": 5
    }
)

GJB = Weapon(
    "Giant Jawblade",
    gs,
    wrk,
    20000,
    8,
    JBI,
    {
        "Hunter Symbol I": 5,
        "Monster Hardbone": 5,
        "Dragonbone Relic": 1,
        "Commission Ticket": 2
    }
)