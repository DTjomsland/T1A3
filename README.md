# T1A3 Python Application

## GitHub Repository: 
https://github.com/DTjomsland/T1A3
<br><br>

## Project Description:
This program was created to make comparing gear in *World of Warcraft: The Burning Crusade* streamlined and simple. It allows the user to input their class and specialization in order to access the appropriate stats that they should be using for their character.  After the inputs have been received, the program prompts the user to enter the stats of their first item.  After all of the stats for item one are collected, it prompts the user for the stats of their second item. Upon collection of both gear stats, the program calculates which item is better for their class based on stat weights and informs the user of the result.
<br>
<br>

## Code Style Guide:
This Python application was styled using the PEP8 guidelines.  These guidelines were followed throughout the creation of the application.  A formatter was used after the application's completion to ensure that all code is styled to PEP8 standards.
<br>
<br>

## Application Features:
### Feature 1: Collection of User Class
The user is prompted to input their class while being provided a list of available options. This input is stored in the variable `player_class`. The variable `player_class` is compared to the keys in the upper level of the `classes` dictionary to make sure it is valid.  If there are not any keys matching `player_class`, the user will be prompted with a while loop to input a valid class until it matches a stored value in the dictionary.  Once `player_class` is assigned a valid value, it will be returned for use in other functions.

### Summary:
Prompts and stores user input for Class. (Ex: Druid, Mage, Shaman)
- Classes displayed are dictionary keys from a separate file used for data storage.
- User input is not case sensitive for ease of use.
- If user input does not match the list provided, it will prompt them to pick a valid one.
<br>
<br>

### Feature 2: Collection of User Specialization
The user is prompted to input their specialization while being provided a list of available options.  These options are displayed based on the class they have entered, meaning only the specializations relevant to their class are valid options.  The variable `specialization` is then compared to keys that are within the selected `player_class` dictionary.  If the value of the variable `specialization` is not found, he user will be prompted with a while loop to input a valid class until it matches a stored value in the dictionary. Once `specialization` is assigned a valid value, it will be returned for use in other functions.

### Summary:
Prompts and stores user input for Specialization. (Ex: Druid: Feral Tank, Feral DPS, Restoration, Balance).
- Specializations displayed are stored dictionary keys that are nested in the previous dictionary.
- This allows for only the relevant specializations to be displayed.
- If user input does not match the list provided, it will prompt them to pick a valid one.
<br>
<br>

### Feature 3: Collection of Item Stats
The user is prompted to input the stats on their first item one by one, until all of the stats have been entered. Only the stats that are relevant to the users class/specialization are prompted.  For example, a feral druid will be asked for physical damage stats such as strength and agility while a balance druid will be asked for spell power and spell crit.  The values must be a float/integer in order for the program to work, so an error handler is implemented in a while loop to be sure the user inputs a number.  These values are collected and put into a new dictionary that was created from the key of the `specialization` dictionary. The new variable `item`, which is a dictionary of the entered stats, is returned for use in other functions.  This is repeated for the user's second item.

### Summary:
Prompts and stores user input for Item 1 + 2 stats (Ex: Strength, Stamina, Intellect)
- The stats that are prompted are only relevant to the specialization chosen. These are nested in the previous dictionary as keys to their own dictionary.  
<br>
<br>

### Feature 4: Calculation of Item Output
Once the stats of both items are collected and stored, their keys will be compared to the keys of the stat weights for the class/spec entered.  If matching, the values will be multiplied together to find the damage output of the individual stats.  This will be returned as `item_calc` for use in other functions.

### Summary:
The values entered are both multiplied by the stat weights stored in a dictionary.
<br>
<br>

### Feature 5: Item Comparison
The variables `item1_calc` and `item2_calc` that are the result of multiplying the user entered stat values by their stat weights will be the variables passed into the comparison.  The sum of both dictionaries' keys will be calculated and then the sums will be compared to determine which item has the higher output.  The item with the higher output will be printed for the user unless their outputs are the same, then the user will be informed the two items are the same. 

### Summary:
- The user is provided a statement informing them which item is better for their chosen specialization.
- The user is also given the number output for its grade/rank.
<br>
<br>

### Feature 6: Restart Program
The user is asked whether they would like to start the program over.  This is not case sensitive for ease of use.

### Summary:
- Y or Yes starts the program over.
- N or No exits the program.
<br>
<br>

## Implementation Plan:
*Each feature relies on the previous one's output, so they will be implemented in order.*

### Dictionary (Priority #1 | Due: 12 July 2022): Classes/Specs/Stat Weights 
Checklist:
- Create a classes variable
- Set the variable equal to a dictionary.
- Outermost dictionary keys are classes and values are dictionaries.
- Second layers dictionary keys are specs and values are dictionaries.
- Third layers dictionary keys are stats and values are stat weights.

### Feature 1 (Priority #2 | Due: 12 July 2022): Collection of User Class
Checklist:
- Print all available classes
- Create input field
- Only allow input that matches available classes
- Create a message if input does not match available classes
- Store the chosen class in a variable
- Return variable for further use.

### Feature 2 (Priority #3 | Due: 12 July 2022): Collection of User Specialization
Checklist:
- Pass through class variable.
- Print all available specializations.
- Create input field for spec.
- Only allow input that matches available specs.
- Create a message if input does not match available specs.
- Store the chosen spec in a variable.
- Return variable for further use.

### Feature 3 (Priority #4 | Due: 13 July 2022): Collection of Item Stats 
Checklist:
- Pass through specialization and class variables.
- Prompt the user to enter the stats for item.
- Only prompt the stats that are relevant to the class/spec combo.
- Create an error handler if input is not a number.
- Store the inputs in a dictionary.
- Return the dictionary for use elsewhere.

### Feature 4 (Priority #5 | Due: 13 July 2022): Calculation of Item Output
Checklist:
- Pass through both user items.
- Multiply values in item1 by stat weights in dictionary.
- Multiply values in item 2 by stat weights in dictionary.
- Create a message if input does not match available specs.
- Create a new variable for each of the outcomes.
- Return the variables for further use.

### Feature 5 (Priority #6 | Due: 14 July 2022): Item Comparison 
Checklist:
- Pass through the variables from the previous function.
- Create variable that contains the sum of all item1's values.
- Create variable that contains the sum of all item2's value.
- Write if statements comparing each of the sums.
- Print which item is the best for the user.

### Feature 6: (Priority #7 | Due: 14 July 2022) Restart Program
- Ask user if they would like to restart or exit the program.
- Provide them if valid inputs.
- Make sure inputs are not case sensitive for ease of use.
- If user wants to restart the program, restart is.
- If user wants to exit, thank them and exit the program.

### Trello Board:
Link: https://trello.com/b/XbyH9zF8/world-of-warcraft-gear-comparison
![](/image/trello.PNG)
![](/image/trellocard.PNG)

### Help Information
## Execute Program:
1. Open terminal
2. Navigate to directory containing application
3. Execute run_app.sh file: Enter `./run_app.sh`
## Steps to install:
1. Install Python3 (To check if Python3 is installed, enter ```python3 --version``` into terminal)
    * Installation instructions: https://realpython.com/installing-python/
2. Install pip3 (To check if pip3 is installed, enter ```pip3 --version``` into terminal)
    * Installation instructions: https://pip.pypa.io/en/stable/installation/
3. Install *colorama* module. (To check for installation, enter ```pip3 list``` into terminal)
    * Installation instructions: Enter ```pip3 install colorama``` into terminal.
4.  Install *art* module. (To check for installation, enter ```pip3 list``` into terminal)
    * Installation instructions: Enter ```pip3 install art``` into terminal.
