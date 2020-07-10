import time
import random

# Definizione degli elementi random
# che si possono trovare nel gioco, e varie direzioni
combat_items = ["gun", "shotgun", "machine gun", "knife", "bow"]
restore_items = ["bottle of water", "sandwich", "hotdog", "tomato",
                                    "banana", "potato"]
items = []
directions = ["straight", "left", "right", "back"]
direction = []
direct = []

# Fa il print degli output singoli/multipli
# e rallenta gli stessi di 2 secondi


def print_time(string):
    print(string)
    time.sleep(2)


def print_multy_time(string):
    index = 0
    while index < len(string):
        print(string[index])
        time.sleep(2)
        index += 1


def choose():
    return input("--> ")


# Intro of the game
def intro():
    global combat_items, restore_items, items

    print_multy_time(["What happens?", "Where I am?",
                     "Who I am?"])

    combat = random.choice(combat_items)
    restore = random.choice(restore_items)

    items.append(combat)
    items.append(restore)

    print_time(f"Around you, there are only a {combat} "
               f"and a {restore}.")

    print_multy_time(["I take everything and get up.",
                     "Everything around is deserted, where should I go?",
                      "Go straight, right, left or back?"])


# The unique randomize system
def raindomize():
    for index in range(len(directions)):
        direction.append(random.choice(directions))
        directions.remove(direction[index])


# 1 Choice
def first_choice_randomize():
    d = choose()
    direct.append(d)

    if direction[0] == direct[0]:
        # OPTION NOTHING
        print_multy_time(["I've been walking for a while, but I haven't found"
                          " anything yet ...", "I'm starting to dehydrate ...",
                          f"Should I consume my {items[1]}? (yes or no)"])
        direct.append(0)

    elif direction[1] == direct[0]:
        # OPTION CAMEL
        print_time("After walking for a while, I found a talking camel.")
        print_time(f"Asks to let him consume mine {items[1]} ... ")
        print_time('What do I answer? (yes or no)')
        direct.append(1)

    elif direction[2] == direct[0]:
        # OPTION WARRIOR
        print_time("After walking for a while, I found a frightening warrior.")
        print_time(f"Asks to let him consume mine {items[1]} ... ")
        print_time('What do I answer? (yes or no)')
        direct.append(2)

    elif direction[3] == direct[0]:
        # OPTION DEATH
        print_time(f"A {random.choice(restore_items)} started to cover me"
                   " with sand until I lost my last breath ...")
        print_time("GAME OVER")
        retry()

    else:
        direct.remove(d)
        first_choice_randomize()


# 2 Choice
def second_choice_consequences():
    choos = input("--> ")
    # OPTION NOTHING - continuing
    if direct[1] == 0 and choos == "yes":
        print_time(f"Okay, now I'm feeling better! Soo good this {items[1]}!")
        print_time("Continuing straight on, I found a village and they"
                   "saved me!")
        print_time("MISSION COMPLETE!")

    elif direct[1] == 0 and choos == "no":
        print_multy_time(["Continuing straight on, without consuming anything",
                          "I start to feel tired.", "I start to hallucinate."])
        print_time(f"A {random.choice(restore_items)} started to cover "
                   " me with sand until I lost my last breath ...")
        print_time("GAME OVER")

    # OPTION CAMEL - continuing
    elif direct[1] == 1 and choos == "yes":
        print_time(f"I give him mine {items[1]}.")
        print_time("Overjoyed, he takes me on his back and takes me to"
                   " the nearest village, saving my life!")
        print_time("MISSION COMPLETE!")

    elif direct[1] == 1 and choos == "no":
        print_time(f"The angry camel takes my {items[0]} in his"
                   " mouth and kills me!")
        print_time("GAME OVER")

    # OPTION 3 - continuing
    elif direct[1] == 2 and choos == "yes":
        print_multy_time([f"Try to give him your {items[1]}.",
                          "But he tries to kill yourself anyway.",
                          f"Luckily you have your {items[0]}, kill him,"
                          "steal its map and save yourself!"])
        print_time("MISSION COMPLETE!")

    elif direct[1] == 2 and choos == "no":
        print_multy_time([f"Your answer angers him and tries to kill you.",
                          f"Luckily you have your {items[0]}, kill him,"
                          "steal its map and save yourself!"])
        print_time("MISSION COMPLETE!")

    else:
        second_choice_consequences()


# Retry
def retry():
    global combat_items, restore_items, items, directions, direction, direct
    again = input("Do you want to try again? (yes or no)")
    if again == "yes":
        combat_items = ["gun", "shotgun", "machine gun",
                        "knife", "bow"]
        restore_items = ["bottle of water", "sandwich",
                         "hotdog", "tomato", "banana", "potato"]
        items = []
        directions = ["straight", "left", "right", "back"]
        direction = []
        direct = []
        main()
    elif again == "no":
        exit()
    else:
        retry()


# Main program
def main():
    intro()
    raindomize()
    first_choice_randomize()
    second_choice_consequences()
    retry()


main()
