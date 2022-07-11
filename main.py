player_class = "druid"


def get_specialization():
    global specialization
    if player_class == "druid":
        specialization = input("Is your specialization balance or feral? ").lower()
        while specialization != "balance" and specialization != "feral":
            specialization = input("Please choose between balance or feral: ").lower()
        return specialization

def get_item1():
    global specialization
    global item1
    print("Please enter stat values for Item 1: ")
    if specialization == "feral":
        item1 = {
            "strength": None,
            "agility": None,
            "intellect": None,
            "stamina": None,
            "hit": None,
            "expertise": None,
            "attack power": None,
            "crit": None,
            "haste": None,
            "armor penetration": None,
        }
        item1["strength"] = int(input("Strength: "))
        item1["agility"] = int(input("Agility: "))
        item1["intellect"] = int(input("Intellect: "))
        item1["stamina"] = int(input("Stamina: "))
        item1["hit"] = int(input("Hit: "))
        item1["expertise"] = int(input("Expertise: "))
        item1["attack power"] = int(input("Attack Power: "))
        item1["crit"] = int(input("Crit: "))
        item1["haste"] = int(input("Haste: "))
        item1["armor penetration"] = int(input("Armor Penetration: "))
        return item1

    
    
    
    
def get_item2():
    global specialization
    global item2
    print("Please enter stat values for Item 2: ")
    if specialization == "feral":
        item2 = {
            "strength": None,
            "agility": None,
            "intellect": None,
            "stamina": None,
            "hit": None,
            "expertise": None,
            "attack power": None,
            "crit": None,
            "haste": None,
            "armor penetration": None,
        }
        item2["strength"] = int(input("Strength: "))
        item2["agility"] = int(input("Agility: "))
        item2["intellect"] = int(input("Intellect: "))
        item2["stamina"] = int(input("Stamina: "))
        item2["hit"] = int(input("Hit: "))
        item2["expertise"] = int(input("Expertise: "))
        item2["attack power"] = int(input("Attack Power: "))
        item2["crit"] = int(input("Crit: "))
        item2["haste"] = int(input("Haste: "))
        item2["armor penetration"] = int(input("Armor Penetration: "))
        return item2

get_specialization()
get_item1()
get_item2()
        
print(item1)
print(item2)