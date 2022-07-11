import class_info
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

def _calculate_stats(player_class, specialization, item):
    item_calc = item
    for k, v in item_calc.items():
        if k in classes[player_class][specialization]:
            item_calc[k] = v * classes[player_class][specialization][k]
    return item_calc

def _compare_items(item1_calc, item2_calc):
    if sum(item1_calc.values()) > sum(item2_calc.values()):
        print("Item 1 provides more damage output than Item 2")
    if sum(item1_calc.values()) < sum(item2_calc.values()):
        print("Item 2 provides more damage output than Item 1")
    if sum(item1_calc.values()) == sum(item2_calc.values()):
        print("The two items provide the same damage output")

def main_function():
    player_class = _get_player_class()
    specialization = _get_specialization(player_class)
    item1 = _get_item(player_class, specialization, 1)
    item2 = _get_item(player_class, specialization, 2)
    item1_calc = _calculate_stats(player_class, specialization, item1)
    item2_calc = _calculate_stats(player_class, specialization, item2)
    _compare_items(item1_calc, item2_calc)

main_function()  







    
