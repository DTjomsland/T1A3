import class_info
from colorama import Fore, Back, Style
from art import *


print(Fore.MAGENTA + text2art('''Dave's TBC Gear Tool''',
      font="small") + Style.RESET_ALL)


def _get_player_class():
    print(Fore.CYAN + 'Please choose one of the following classes: \n' + Style.RESET_ALL)
    print(*list(class_info.classes.keys()), sep="   ")
    print()
    player_class = input('Your Class: ').title()
    print()
    while player_class not in list(class_info.classes.keys()):
        print(Fore.YELLOW + 'Please choose a valid class. \n' + Style.RESET_ALL)
        player_class = input('Your Class: ').title()
        print()
    return player_class


def _get_specialization(player_class):
    print(Fore.CYAN + 'Please choose one of the following specializations: \n' + Style.RESET_ALL)
    print(*list(class_info.classes[player_class].keys()), sep="   ")
    print()
    specialization = input('Your Specialization: ').title()
    print()
    while specialization not in list(class_info.classes[player_class].keys()):
        print(Fore.YELLOW + "Please choose a valid specialization. \n" + Style.RESET_ALL)
        specialization = input('Your Specialization: ').title()
        print()
    return specialization


def _get_item(player_class, specialization, number):
    item = {}
    print(Fore.CYAN +
          f"Please enter stat values for Item {number}: \n" + Style.RESET_ALL)
    for k, v in class_info.classes[player_class][specialization].items():
        item[k] = None
    for k, v in item.items():
        while True:
            try:
                item[k] = float(input(str(k).title() + ": "))
            except ValueError:
                print(
                    Fore.YELLOW + f'{k.title()} must be a numerical value.' + Style.RESET_ALL)
            else:
                break
    print()
    return item


def _calculate_stats(player_class, specialization, item):
    item_calc = item
    for k, v in item_calc.items():
        if k in class_info.classes[player_class][specialization]:
            item_calc[k] = v * \
                class_info.classes[player_class][specialization][k]
    return item_calc


def _compare_items(item1_calc, item2_calc):
    if sum(item1_calc.values()) > sum(item2_calc.values()):
        print(Fore.GREEN + "Item 1 provides more output than Item 2 \n" + Style.RESET_ALL)
    if sum(item1_calc.values()) < sum(item2_calc.values()):
        print(Fore.GREEN + "Item 2 provides more output than Item 1 \n" + Style.RESET_ALL)
    if sum(item1_calc.values()) == sum(item2_calc.values()):
        print(Fore.GREEN + "The two items provide the same output \n" + Style.RESET_ALL)


def _restart():
    restart = input(
        Fore.CYAN + "Would you like to restart this program? (Y/N) \n" + Style.RESET_ALL)
    print()
    if restart == "yes" or restart == "y":
        main_function()
    if restart == "n" or restart == "no":
        print(Fore.GREEN + "Thanks for choosing Dave's Gear Comparison Tool.  Goodbye!" + Style.RESET_ALL)


def main_function():
    player_class = _get_player_class()
    specialization = _get_specialization(player_class)
    item1 = _get_item(player_class, specialization, 1)
    item2 = _get_item(player_class, specialization, 2)
    item1_calc = _calculate_stats(player_class, specialization, item1)
    item2_calc = _calculate_stats(player_class, specialization, item2)
    _compare_items(item1_calc, item2_calc)
    _restart()


main_function()