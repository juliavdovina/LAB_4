"""Module for game"""

class Street:
    """
    class for room
    """
    def __init__(self, street: str) -> None:
        """main function"""
        self.street = street
        self.description = None
        self.character = None
        self.item = None
        self.sides_of_the_world = {}

    def set_description(self, description: str) -> str:
        """street's description"""
        self.description = description

    def link_room(self, another_street: 'Street', side: str) -> None:
        """this function add a new key(side of the world) and value(street) to the dictionary"""
        self.sides_of_the_world[side] = another_street

    def get_details(self) -> str:
        """this function returns details of street and game's process"""
        print(f"{self.street}\n--------------------\n{self.description}")
        for part, street in self.sides_of_the_world.items():
            print(f"The {street.street} is {part}")

    def set_character(self, character) -> None:
        """this function set a character"""
        self.character = character

    def set_item(self, item: 'Item') -> None:
        """this function set an item"""
        self.item = item

    def get_character(self) -> str:
        """this function returns character"""
        return self.character

    def get_item(self) -> str:
        """this function returns item"""
        return self.item

    def move(self, command: str) -> str:
        """this function returns move to another street"""
        return self.sides_of_the_world[command]


NUMBER = 0
class Character:
    """class for character"""
    def __init__(self, name: str, description: str) -> None:
        """main function"""
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None


class Lotr(Character):
    """class for lotr"""
    def __init__(self, name: str, description: str) -> None:
        """main function"""
        super().__init__(name, description)
        self.conversation = None
        self.weakness = None

    def set_conversation(self, phrase: str) -> None:
        """this function set a conversation"""
        self.conversation = phrase

    def set_weakness(self, weakness: str) -> None:
        """this function set a enemy's weakness"""
        self.weakness = weakness

    def describe(self) -> str:
        """this function returns sentence"""
        print(f'{self.name} is here!\n{self.description}')

    def talk(self) -> str:
        """this function returns phrase"""
        print(f'[{self.name} says]: {self.conversation}')

    def fight(self, item: str) -> bool:
        """this function check if a character is weak in the item"""
        if item == self.weakness:
            global NUMBER
            NUMBER += 1
            print(f"You fend {self.name} off with the {self.weakness}")
            return True
        print(f"{self.name} crushes you, puny adventurer!")
        return False

    def get_defeated(self) -> int:
        """this function returns the number of defeated"""
        return NUMBER


class Homeless(Character):
    """class for homeless"""
    def __init__(self, name: str, description: str) -> None:
        """main function"""
        super().__init__(name, description)
        self.conversation = None
        self.weakness = None

    def set_conversation(self, phrase: str) -> None:
        """this function set a conversation"""
        self.conversation = phrase

    def set_weakness(self, weakness: str) -> None:
        """this function set a enemy's weakness"""
        self.weakness = weakness

    def describe(self) -> str:
        """this function returns sentence"""
        print(f'{self.name} is here!\n{self.description}')

    def talk(self) -> str:
        """this function returns phrase"""
        print(f'[{self.name} says]: {self.conversation}')

    def fight(self, item: str) -> bool:
        """this function check if a character is weak in the item"""
        if item == self.weakness:
            global NUMBER
            NUMBER += 1
            print(f"You fend {self.name} off with the {self.weakness}")
            return True
        print(f"{self.name} crushes you, puny adventurer!")
        return False

    def get_defeated(self) -> int:
        """this function returns the number of defeated"""
        return NUMBER


class Policeman(Character):
    """class for policeman"""
    def __init__(self, name: str, description: str) -> None:
        """main function"""
        super().__init__(name, description)
        self.conversation = None
        self.weakness = None

    def set_conversation(self, phrase: str) -> None:
        """this function set a conversation"""
        self.conversation = phrase

    def set_weakness(self, weakness: str) -> None:
        """this function set a enemy's weakness"""
        self.weakness = weakness

    def fight(self, item: str) -> bool:
        """this function check if a character is weak in the item"""
        if item == self.weakness:
            global NUMBER
            NUMBER += 1
            print(f"You fend {self.name} off with the {self.weakness}")
            return True
        print(f"{self.name} crushes you, puny adventurer!")
        return False

    def get_defeated(self) -> int:
        """this function returns the number of defeated"""
        return NUMBER

    def describe(self) -> str:
        """this function returns sentence"""
        print(f'{self.name} is here!\n{self.description}')

    def talk(self) -> str:
        """this function returns phrase"""
        print(f'[{self.name} says]: {self.conversation}')


class Item:
    """class for item"""
    def __init__(self, title: str) -> None:
        """main function"""
        self.title = title
        self.description = None

    def set_description(self, description: str) -> str:
        """item's description"""
        self.description = description

    def get_name(self) -> str:
        """this function returns item's name"""
        return self.title

    def describe(self) -> str:
        """this function returns description"""
        print(f'The [{self.title}] is here - {self.description}')
