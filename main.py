import class_info

from art import *

print(text2art('''Dave's TBC Gear Tool''', font="small"))

def _get_player_class():
    print('Please pick one of the following classes: ')
    print(*list(class_info.classes.keys()), sep="   ")
    player_class = input('Your Class: ').title()
    while player_class not in list(class_info.classes.keys()):
        player_class = input('Please choose a valid class: ').title()
    return player_class

def _get_specialization(player_class):
    print('Please pick one of the following specializations:')
    print(*list(class_info.classes[player_class].keys()), sep="   ")
    specialization = input('Your specialization: ').title()
    while specialization not in list(class_info.classes[player_class].keys()):
        specialization = input('Please choose a valid specialization:').title()
    return specialization

def _get_item(player_class, specialization, number):
    item = {}
    print(f"Please enter stat values for Item {number}: ")
    for k, v in class_info.classes[player_class][specialization].items():
        item[k] = None   
    for k, v in item.items():
        while True:
            try:
                item[k] = float(input(str(k).title() + ": "))
            except ValueError:
                print('Please enter a numerical value.')
            else:
                break
    return item

def _calculate_stats(player_class, specialization, item):
    item_calc = item
    for k, v in item_calc.items():
        if k in class_info.classes[player_class][specialization]:
            item_calc[k] = v * class_info.classes[player_class][specialization][k]
    return item_calc

def _compare_items(item1_calc, item2_calc):
    if sum(item1_calc.values()) > sum(item2_calc.values()):
        print("Item 1 provides more output than Item 2")
    if sum(item1_calc.values()) < sum(item2_calc.values()):
        print("Item 2 provides more output than Item 1")
    if sum(item1_calc.values()) == sum(item2_calc.values()):
        print("The two items provide the same output")

def main_function():
    player_class = _get_player_class()
    specialization = _get_specialization(player_class)
    item1 = _get_item(player_class, specialization, 1)
    item2 = _get_item(player_class, specialization, 2)
    item1_calc = _calculate_stats(player_class, specialization, item1)
    item2_calc = _calculate_stats(player_class, specialization, item2)
    _compare_items(item1_calc, item2_calc)

def restart():
    restart = input("Would you like to restart this program? ")
    if restart == "yes" or restart == "y":
        main_function()
    if restart == "n" or restart == "no":
        print("Thanks for choosing Dave's Gear Comparison Tool.  Goodbye!")

main_function()  
restart()






    
