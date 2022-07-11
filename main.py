classes = {
    "Warlock": {
         "Demonology": {
            "strength": 2.27,
            "agility": 3.61,
            "intellect": 0.38,
            "stamina": 0.17,
            "hit": 1.00,
            "expertise": 3.28,
            "attack power": 1.00,
            "crit": 2.54,
            "haste": 1.53,
            "armor penetration": 0.47,
            },
        },
    "Druid": {
        "Feral": {
            "strength": 2.27,
            "agility": 3.61,
            "intellect": 0.38,
            "stamina": 0.17,
            "hit": 1.00,
            "expertise": 3.28,
            "attack power": 1.00,
            "crit": 2.54,
            "haste": 1.53,
            "armor penetration": 0.47,
            },
        "Balance": {
            "intellect": 2.27,
            "spirit": 3.61,
            "spell damage": 0.38,
            "arcane damage": 0.17,
            "nature damage": 1.00,
            "spell hit": 3.28,
            "spell crit": 1.00,
            "spell haste": 2.54,
            "mp5": 1.53,
        }
    }
}


def _get_player_class():
    print('Please pick one of the following classes:')
    print(*list(classes.keys()), sep="\t")
    player_class = input('Your Class: ').title()
    while player_class not in list(classes.keys()):
        player_class = input('Please choose a valid class: ').title()
    return player_class

def _get_specialization(player_class):
    print('Please pick one of the following specializations:')
    print(*list(classes[player_class].keys()), sep="\t")
    specialization = input('Your specialization: ').title()
    while specialization not in list(classes[player_class].keys()):
        specialization = input('Please choose a valid specialization:').title()
    return specialization

def _get_item(player_class, specialization, number):
    item = {}
    print(f"Please enter stat values for Item {number}: ")
    for k, v in classes[player_class][specialization].items():
        item[k] = None   
    for k, v in item.items():
        item[k] = int(input(str(k).title() + ": "))
    return item

def main_function():
    player_class = _get_player_class()
    specialization = _get_specialization(player_class)
    item1 = _get_item(player_class, specialization, 1)

main_function()  







    
