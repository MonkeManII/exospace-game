loot_table = ""
is_complete = False
item_names = [
    "Mossy Stone",
    "Stone",
    "Forest Log",
    "Forest Plank",
    "Forest Leaves",
    "Gemfruit",
    "Mixed Berry Seeds",
    "Wooden Pickaxe",
    "Stone Pickaxe",
    "Metal Pickaxe",
    "Gem Pickaxe",
    "Gilded Pickaxe",
    "Metal Chunk",
    "Gravitite",
    "Metal Ingot",
    "Verdite",
    "Voidstone",
    "Water",
    "Heart Berry",
    "Compass",
    "Void Berry",
    "Gemfruit Bulbs",
    "Heart Berry Seeds",
    "Void Berry Seeds",
    "Cosmic Grain",
    "Cosmic Grain Seeds",
    "Bottle",
    "Gemfruit Smoothie",
    "Heartberry Juice",
    "Voidberry Cocktail",
    "Glass",
    "Gravel",
    "Sand",
    "Stick",
    "Rope",
    "Wooden Hatchet",
    "Wooden Shovel",
    "Stone Hatchet",
    "Stone Shovel",
    "Torch",
    "Lava",
    "Sparkpowder",
    "Coal",
    "Flint",
    "Simple Pot",
    "Chest",
    "Metal Hatchet",
    "Metal Shovel",
    "Pocket Anvil",
    "Bolt",
    "Toxic Gas",
    "Wire",
    "Gobite Ingot",
    "Raw Gobite",
    "Gobite Lamp",
    "Power Cell",
    "Metal Knife",
    "Hammer",
    "Magma Rock",
    "Augite",
    "Mossy Augite",
    "Cryotite Pearl",
    "Metal Broadsword",
    "Stone Sword",
    "Wooden Sword",
    "Gravitite Engine",
    "Metal Panel",
    "Rocket",
    "Fuel Barrel",
    "Ice",
    "Fireproof Helmet",
    "Fireproof Suit",
    "Fireproof Boots",
    "Radioactive Dust",
    "Glowing Crystal",
    "Crystal Shard",
    "Nuclear Fuel",
    "Familiar Painting",
    "Platemail Helmet",
    "Platemail Chestplate",
    "Platemail Boots",
    "Roll of Insulation",
    "Metal Ring",
    "Overgrown Ring",
    "Radioactive Ring",
    "Electric Ring",
    "Charm of Pacifism",
    "Charm of Satiety",
    "Charm of Recovery",
    "Monitor",
    "Bean",
    "Getato",
    "Getato Eye",
    "Bowl",
    "Fruit Salad",
    "Mashed Getato",
    "Salt",
    "Dough",
    "Pie Crust",
    "Gemfruit Pie",
    "Heartberry Pie",
    "Voidberry Pie",
    "Whisk Spatula",
    "Bread",
    "Rich Soil",
    "Astral Locator",
    "Warp Essence",
    "Warp Crystal",
]

item_ids = [
    "moss",
    "stone",
    "log",
    "planks",
    "leaf",
    "fruit",
    "seed",
    "woodenpickaxe",
    "stonepickaxe",
    "ironpickaxe",
    "diamondpickaxe",
    "gildedpickaxe",
    "rawiron",
    "gravitite",
    "ironbar",
    "verdite",
    "voidstone",
    "water4-0",
    "heartberry",
    "compass",
    "voidberry",
    "fruit-seeds",
    "heartberry-seeds",
    "voidberry-seeds",
    "cosmic-wheat",
    "cosmic-wheat-seeds",
    "bottle",
    "gemsmoothie",
    "heartjuice",
    "voidessence",
    "glass",
    "gravel",
    "moonsand",
    "woodenrod",
    "rope",
    "woodenhatchet",
    "woodenshovel",
    "stonehatchet",
    "stoneshovel",
    "torch",
    "lava4-0",
    "powder",
    "coal",
    "flint",
    "simplepot",
    "chest",
    "ironhatchet",
    "ironshovel",
    "anvil",
    "bolt",
    "toxicgas",
    "wire",
    "gobitebar",
    "rawgobite",
    "gobitelamp",
    "powercell",
    "irondagger",
    "hammer",
    "magmarock",
    "augite",
    "mossyaugite",
    "cryotitepearl",
    "ironsword",
    "stonesword",
    "woodensword",
    "engine",
    "metalpanel",
    "goodrocket",
    "fuel",
    "ice",
    "fireproof_helmet",
    "fireproof_suit",
    "fireproof_boots",
    "radioactivedust",
    "greencrystalshard",
    "purplecrystalshard",
    "nuclearfuel",
    "familiarpainting",
    "plate_helmet",
    "plate_suit",
    "plate_boots",
    "insulation",
    "ironring",
    "overgrownring",
    "radiationring",
    "stunring",
    "healthcharm",
    "foodcharm",
    "recoverycharm",
    "monitoritem",
    "b e a n",
    "tater",
    "tatereye",
    "bowl",
    "fruitsalad",
    "mashedgetato",
    "salt",
    "dough",
    "pie_crust",
    "gemfruit_pie",
    "heartberry_pie",
    "voidberry_pie",
    "whiskspatulathing",
    "bread",
    "richsoil",
    "astrallocator",
    "warpessence",
    "warpcrystal",
]


def get_item_id_by_name(name: str):
    i = 0
    for c_name in item_names:
        if c_name == name:
            print("Item found! (id " + str(i + 1) + ")")
            return i + 1
        i += 1

    i = 0
    for c_id in item_ids:
        if c_id == name:
            print("Item found! (id " + str(i + 1) + ")")
            return i + 1
        i += 1
    print("No such item found.")
    return -1


def prompt_positive_int(msg, allowZero: bool = False):
    _return = -1
    while _return == -1:
        _return = input(msg)
        try:
            _return = int(_return)
        except:
            _return = -1
            print("Return must be integer!")
            continue

        if _return < 0 and allowZero:
            _return = -1
            print("Return must be greater than zero!")
            continue
    return _return


def prompt_mag_float(msg):
    _return = -1
    while _return == -1:
        _return = input(msg)
        try:
            _return = float(_return)
        except:
            print("Return must be a float!")
            continue

        if _return < 0 or _return > 1:
            _return = -1
            print("Return must be within range 0..1 (inclusive)")
            continue
    return _return


def prompt_string_from_options(question, options):
    pick = None
    while pick == None:
        for option in options:
            print(">> " + str(option))
        pick = input(question)

        try:
            pick = str(pick)
        except:
            pick = None
            print("Pick must be a string!")
            continue

        if not pick in options:
            pick = None
            print("Please select a valid option.")
            continue
    return pick


if prompt_string_from_options("Do you wish to load a loot table?", ["Y", "N"]) == "Y":
    loot_table = str(input("Loot table?"))

while not is_complete:
    choice = prompt_string_from_options("Select an action", ["Add Item", "Exit"])
    if choice == "Add Item":
        item_type = "-1"
        while item_type == "-1":
            item_type = str(
                get_item_id_by_name(input("What's the name / sprite of the item?"))
            )
        min_count = None
        max_count = None
        if (
            prompt_string_from_options(
                "For count, do you wish to use...", ["Fixed Count", "Min Max"]
            )
            == "Fixed Count"
        ):
            item_count = str(prompt_positive_int("How much?", True))
            min_count = item_count
            max_count = item_count
        else:
            min_count = str(prompt_positive_int("Min?"))
            max_count = str(prompt_positive_int("Max?"))

        probability = prompt_mag_float("How common do you want this to be?")

        conf = print(
            "Just to confirm, you want to add ID "
            + item_type
            + " with count "
            + min_count
            + ".."
            + max_count
            + " with a "
            + str(probability * 100)
            + "% chance?"
        )
        if prompt_string_from_options("(Y/N)", ["Y", "N"]) == "Y":
            if len(loot_table) > 0:
                loot_table += "|"
            loot_table += (
                item_type + "|" + min_count + "|" + max_count + "|" + str(probability)
            )
        elif choice == "QGen":
            inpt = str(input("ID?"))
            loot_table = inpt + "|1|1|1"
        else:
            print("Addition cancelled!")
            continue
    else:
        is_complete = True
    print("Current loot table: " + loot_table)

print("YOUR END LOOT TABLE (COPY AND PASTE INTO EXOSPACE)")
print(loot_table)
