"""Module for game's process"""
import another_game

ucu = another_game.Street("Kozelnytska")
ucu.set_description("Street where the campus is located.")

park = another_game.Street("Stryiska")
park.set_description("A street with a large park for walking.")

cinema = another_game.Street("Shevchenko")
cinema.set_description("Street where the cinema is located.")

ucu.link_room(park, "north")
park.link_room(ucu, "south")
park.link_room(cinema, "west")
cinema.link_room(park, "east")

serg = another_game.Homeless("Sergiy", "A strange men with dog Rex.")
serg.set_conversation("Tell me what time it is.")
serg.set_weakness("alcohol")
park.set_character(serg)

vadym = another_game.Lotr("Vadym", "A street thief with dark eyes and dark clothes.")
vadym.set_conversation("Can I use your mobile phone to make a call?")
vadym.set_weakness("mobile phone")
cinema.set_character(vadym)

oleksandr = another_game.Policeman("Oleksandr", "A policeman who patrols in the city.")
oleksandr.set_conversation("Good day! Show your documents.")
oleksandr.set_weakness("money")
ucu.set_character(oleksandr)

alcohol = another_game.Item("alcohol")
alcohol.set_description("Any kind of alcohol")
park.set_item(alcohol)

phone = another_game.Item("mobile phone")
phone.set_description("A device that costs a lot of money")
cinema.set_item(phone)

money = another_game.Item("money")
money.set_description("A bad way to avoid responsibility'")
ucu.set_item(money)

current_room = ucu
backpack = []

dead = False

print('commands in the terminal:\n"talk" - you can talk to the characters\n\
"take" - you can take items if they are in the street\n\
"fight" - you can fight with the characters\nor you can input sides of the world')

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with):
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.character = None
                    if inhabitant.get_defeated() == 3:
                        print("Congratulations, you have defeated the enemy!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
