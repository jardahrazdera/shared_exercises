class Room:
    def __init__(self, name, description,):
        self.name = name
        self.description = description
        self.exits = {}

    def add_exit(self,direction, room):
        self.exits[direction] = room

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.room = starting_room

    def move(self,direction):
        if direction in self.room.exits:
            self.room = self.room.exits[direction]
            print(f"You move {direction}.")
        else:
            print("You can't go that way!")

print("Welcome to the Scary Castle Game!\n"
      "If you want to quit during the game,\n"
      "you can type 'quit', 'exit' or 'q'.\n")

hall = Room("hall", "This is the main hall of the scary castle.")
kitchen = Room("kitchen", "Hmm, creapy smoky castle kitchen.")
dining_room = Room("dining Room", "This is the old castle dining room.")
secret_room = Room("secret Room", "You are in the scary secret room. Guess what's next?")
outside = Room("outside", "Breeth deaply and find the way to the castle.")
treasure_room = Room("treasure Room", "Wow! You found the treasure room!")

hall.add_exit("west", secret_room)
secret_room.add_exit("east", hall)

hall.add_exit("east", dining_room)
dining_room.add_exit("west", hall)

hall.add_exit("south", kitchen)
kitchen.add_exit("north", hall)

hall.add_exit("north", outside)
outside.add_exit("south", hall)

secret_room.add_exit("west", treasure_room)
treasure_room.add_exit("east", secret_room)

player = Player("Player", hall)

while True:
    print(f"You are in {player.room.name}")
    print(player.room.description)

    available_exits = ", ".join(player.room.exits.keys())
    print(f"Available exits are: {available_exits}")

    command = input(">>>").lower().strip()
    
    if command == "quit" or command == "exit" or command == "q":
        print("Goodbye, thanks for playing!")
        break
    elif command in player.room.exits:
        player.move(command)
        if player.room == treasure_room:
            print("Congratulations! You found the treasure room. You win!\n"
                  "May be you rich now, but not enough smart yet :)\n")
            break
    else:
        print("I don't understand that command or you can't go that way.\n")