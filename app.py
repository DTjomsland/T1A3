import class_info
import sys
from colorama import Fore, Style
from art import *

# Prints class options from dictionary.
# Prompts user to input their class and stores it in "player_class" variable.  
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

# Prints specialization options from dictionary (based on player_class variable).
# Prompts user to input their specialization and stores it in "specialization" variable.
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

# Prompts items stat input.  Prompts are printed from dictionary (based on player_class/specialization variable).
# Stores the user's item stats in "item" variable.
def _get_item(player_class, specialization, number):
    item = {}
    print(Fore.CYAN + f"Please enter stat values for Item {number}: \n" + Style.RESET_ALL)
    for k, v in class_info.classes[player_class][specialization].items():
        item[k] = None
    for k, v in item.items():
        while True:
            try:
                item[k] = float(input(str(k).title() + ": "))
            except ValueError:
                print(Fore.YELLOW + f'{k.title()} must be a numerical value.' + Style.RESET_ALL)
            else:
                break
    print()
    return item

# Multiplies the item stats by the weights store in the classes dictionary and returns a new dictionary with the values named item_calc.
def _calculate_stats(player_class, specialization, item):
    item_calc = item.copy()
    for k, v in item_calc.items():
        if k in class_info.classes[player_class][specialization]:
            item_calc[k] = v * class_info.classes[player_class][specialization][k]
    return item_calc

# Finds the sum of each item's dictionary values and stores them in variables item1_output and item2_output. 
# Compares item1_output and item2_output to see which number is greater and informs the user.
def _compare_items(item1_calc, item2_calc):
    item1_output = round(sum(item1_calc.values()), 2)
    item2_output = round(sum(item2_calc.values()), 2)
    if item1_output > item2_output:
        print(Fore.GREEN + f"Item 1 ({item1_output}) provides more output than Item 2 ({item2_output}) \n" + Style.RESET_ALL)
        return "item1"
    if item1_output < item2_output:
        print(Fore.GREEN + f"Item 2 ({item2_output}) provides more output than Item 1 ({item1_output}) \n" + Style.RESET_ALL)
        return "item2"
    if item1_output == item2_output:
        print(Fore.GREEN + f"The two items provide the same output ({item1_output}) \n" + Style.RESET_ALL)
        return "equal"

# Gives the user the option to restart the program.
def _restart():
    while True:
        response = input(Fore.CYAN + "Would you like to restart this program? (Y/N) \n" + Style.RESET_ALL).lower()
        print()
        if response == "yes" or response == "y":
            main()
        if response == "n" or response == "no":
            print(Fore.MAGENTA + "Thanks for choosing Dave's TBC Armor Tool.  Goodbye! \n" + Style.RESET_ALL)
            sys.exit()

# Main function. 
def main():
    print(Fore.MAGENTA + text2art('''Dave's TBC Armor Tool''', font="small") + Style.RESET_ALL)
    player_class = _get_player_class()
    specialization = _get_specialization(player_class)
    item1 = _get_item(player_class, specialization, 1)
    item2 = _get_item(player_class, specialization, 2)
    item1_calc = _calculate_stats(player_class, specialization, item1)
    item2_calc = _calculate_stats(player_class, specialization, item2)
    _compare_items(item1_calc, item2_calc)
    _restart()

if __name__ == "__main__":
    main()