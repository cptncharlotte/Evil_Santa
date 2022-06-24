room1 =(
    1,#room number
    "Welcome to the start of the game Evil Santa",#greeting
    ["key"],#objects
    [ #doors list
        ["e", 2, False],# direction, destination, is it locked no but true is locked
        ["s", 6, False]]
    )
room2 =(
    2,
    "Welcome to room two",
    [],
    [
        ["e", 3, True],
        ["s", 7, False],
        ["w", 1, False]]
    )
room3 =(
    3,
    "welcome to room three",
    ["christmas_magic"],
    [
        ["s", 8, False],
        ["e", 4, False],
        ["w", 2, False]]
    )
room4 =(
    4,
    "welcome to room four",
    ["Elf"],
    [
        ["e", 5, True],
        ["s", 9, False],
        ["w", 3, False]]
    )

room5 =(
    5,
    "Welcome to room five",
    [],
    [
        ["s", 14, True],
        ["w", 4, False]]
    )
room6 =(
    6,
    "welcome to room six",
    [],
    [
        ["s", 10, False],
        ["n", 3, False]]
    )
room7 =(
    7,
    "welcome to room sevan",
    ["Santa_Plush"],
    [
        ["n", 2, False]]
    )

room8 =(
    8,
    "welcome to room eight",
    ["Jukebox"],
    [
        ["n", 3, False]]
    )
room9 =(
    9,
    "welcome to room nine",
    ["key"],
    [
        ["n", 4, False]]
    )
room10 =(
    10,
    "welcome to room ten",
    [""],
    [
        ["n", 6, False],
        ["e", 11,False]]
    )
room11 =(
    11,
    "welcome to room eleven",
    ["key"],
    [
        ["w", 10, False]]
    )
room12 =(
    12,
    "welcome to room twelve",
    [""],
    [
        ["n", 10, False],
        ["e",13, False],
        ["s",14,True]]
    )
room13 =(
    13,
    "welcome to room thirteen",
    ["portal_key"],
    [
        ["w",12,False]]
    )
room14 =(
    14,
    "welcome to room fourteen",
    ["portal"],
    [
        ["n",12,True]]
    )
# This dictionary contains all the rooms
rooms = {
        1: room1,
        2: room2,
        3: room3,
        4: room4,
        5: room5,
        6: room6,
        7: room7,
        8: room8,
        9: room9,
        10: room10,
        11: room11,
        12: room12,
        13: room13,
        14: room14
    }

def show_room(room):
    (number, greeting, objects, doors) = room
    
    #print the greeting
    print(greeting)
    print("-------------------------------------------")
    #list the inventory
    print("You have the following items:")
    for item in inventory:
        print("* " + item)
    print()
    
    #list objects
    print("You see the following item:")
    for item in objects:
        print(item)
        
    #list exits
    print("you see the following exits:")
    
    for door in doors:
        (direction, dest, locked) = door
        
        if locked:
            print("* " + direction + " (locked)")
        else:
            print("* " + direction)

def go(direction):
    """
    moves from the current room.
    parameteres:
    ------------
    direction (string): the direction to move (n, e, w,s)
    
    updates the current_room if the room is valid.
    """
    global current_room
    global rooms
    doors = current_room[3]
    
    objects = current_room[2]
    if current_room[0] == 4:
        if "elf" in objects:
            print("You were lucky! The elf sits in a corner and sulks as you walk out the room.")
    if current_room[0] == 5:
        if "santa" in objects:
            print("Santa drags you back into his lair and strangles you with tinsel! You are dead.")
            exit()
            
    for door in doors:
        (door_direction, destination, locked) = door
        if door_direction == direction:
            if locked:
                print("That door is locked. No entry....!")
                print()
            else:
                current_room = rooms[destination]
                return
    
    print("Sorry, you can't go there.")
    
    
    
    
def take(thing):
    """
    Takes an object - remove it from the room, add it to inventory
    Parameters:
    -----------
    thing (str): the object to take
    """
    global current_room
    global inventory
    
    # check if the item is in the room
    objects = current_room[2]
    if(thing in objects):
        # add item to inventory
        inventory.append(thing)
        # remove item from room
        objects.remove(thing)
    else:
        # warn user item is not in the room
        print("I can't see that check the objects")
        
def unlock():
    """
    unlock all of the doors in the current room
    """
    global current_room
    
    doors = current_room[3]
    #doors is a list of tupels, like ("e", 3, True)
    for door in doors:
        # unlock the doors
        door[2] = False
        
        
        
def christmas_magic():
    """
    Kills the elf if present
    """
    global current_room
    global rooms
    
    print("in christmas_magic")
    # TODO: if the elf is in the room, kill him
    objects = current_room[2]
    if "Elf" in objects:
        #TODO kill elf
        objects.remove("Elf")
        print("You throw the christmas magic over the elf, killing it")
    else:
        # TODO: wasted... remove christmas_magic back to the christmas_magic room
        christmas_magic_room = rooms[3]
        print("no elf, wasted")
        
        
def use(thing):
    """
    uses the specified thing in the current room.
    Parameters:
    -----------
    thing (str): the thing to use
    """
    global inventory
    global current_room
    global rooms
    
    #TODO: check that thing is in inventory
    thing = thing.lower()
    if (thing in inventory):
        #TODO: an if statement for each supported thing
        # valid things to use: "christmas_magic", "elf", "santa_plush", "jukebox", "key, Grinch"
        if thing == "christmas_magic":
            christmas_magic()
        elif thing == "santa_plush":
            print("You give the santa plush a big hug. awwwwwwwwww!")
        elif thing == "jukebox":
            print("the jukebox plays some wonderful christmas music")
        elif thing == "key":
            unlock()
        elif thing == "grinch":
            print("I hate christmas. says the grinch")
        elif thing == "portal":  
            print("Everything goes wobbly for a moment...")
            current_room = rooms[5]
        elif thing == "portal_key":
            if current_room[0] == 12:
                unlock()
            else:
               print("The portal key only unlocks a certain door...")
        elif thing == "santa":
            print("you shall never defeat me says evil santa")
        else:
            print("I don't know how to us a " + thing)
    else:
        #TODO: warn the user that they dont have the object
        print("you dont have that")

#the main event loop
current_room = rooms[1]


#set up strating room
inventory = []


# game loop
while True:
    show_room(current_room)
    #room_num = int(input("Enter a room number: "))
    #current_room = rooms[room_num]
    cmd = input("enter command> ")
    cmd_bits = cmd.split(' ')
    verb = cmd_bits[0]
    noun = cmd_bits[1]
    #Dad wrote Action (= verb) and Qualifier (= noun) instead of noun and verb
    print("verb: " + verb)
    print("noun: " + noun)
    
    verb = verb.lower()
    noun = noun.lower()
    if verb == "go":
        go(noun)
    elif verb == "take":
        take(noun)
    elif verb == "use":
        use(noun)
    else:
        print("invalid command! NO HACKING ALLOWED!")
        print("------------------------------------")
        