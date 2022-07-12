# T1A3 Python Application

## GitHub Repository: 
https://github.com/DTjomsland/T1A3

## Project Description:
This program was created to make comparing gear in *World of Warcraft: The Burning Crusade* streamlined and simple. It allows the user to input their class and specialization in order to access the appropriate stats that they should be using for their character.  After the inputs have been received, the program prompts the user to enter the stats of their first item.  After all of the stats for item one are collected, it prompts the user for the stats of their second item. Upon collection of both gear stats, the program calculates which item is better for their class based on stat weights. 

## Code Style Guide:
This Python application was styled using the PEP8 guidelines.  These guidelines were followed throughout the creation of the application.  A formatter was used after the application's completion to ensure that all code is styled to PEP8 standards.

## Application Features:
### Feature 1: Collection of User Class
The user is prompted to input their class while being provided a list of available options. This input is stored in the variable `player_class`. The variable `player_class` is compared to the keys in the upper level of the `classes` dictionary to make sure it is valid.  If there are not any keys matching `player_class`, the user will be prompted with a while loop to input a valid class until it matches a stored value in the dictionary.  Once `player_class` is assigned a valid value, it will be returned for use in other functions.

### Feature 2: Collection of User Specialization
The user is prompted to input their specialization while being provided a list of available options.  These options are displayed based on the class they have entered, meaning only the specializations relevant to their class are valid options.  The variable `specialization` is then compared to keys that are within the seleceted `player_class` dictionary.  If the value of the variable `specialization` is not found, he user will be prompted with a while loop to input a valid class until it matches a stored value in the dictionary. Once `specialization` is assigned a valid value, it will be returned for use in other functions.

### Feature 3: Collection of Item Stats
The user is prompted to input the stats on their first item one by one, until all of the stats have been entered. Only the stats that are relevant to the users class/specialization are prompted.  For example, a feral druid will be asked for physical damage stats such as strength and agility while a balance druid will be asked for spell power and spell crit.  The values must be a float/integer in order for the program to work, so an error handler is implemented in a while loop to be sure the user inputs a numnber.  These values are collected and put into a new dictionary that was created from the key of the `specialization` dictionary. The new variable `item`, which is a dictionary of the entered stats, is returned for use in other functions.  This is repeated for the user's second item.

### Feature 4: Calculation of Item Output
Once the stats of both items are collected and stored, their keys will be compared to the keys of the stat weights for the class/spec entered.  If matching, the values will be multiplied together to find the damage output of the individual stats.  This will be returned as `item_calc` for use in other functions.

### Feature 5: Item Comparison
The dictionaries containing the values that were the result of multiplying the stat values by their stat weights will be the variables passed into the comparison.  The sum of both dictionaries' keys will be calculated and then the sums will be compared to determin which item has the higher output.  The item with the higher output will be printed for the user unless their outputs are the same, then the user will be informed the two items are the same. 



