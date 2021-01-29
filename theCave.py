from sys import exit
import time

# Sets global variables
hp = 20
leaveRoom = False
skeleTreasure = False

def border():
    print("\n****************************************************************************************************\n")

def look(room):
    # Prints the top border of look
    border()
    print("You take a look around.\n")

    if room == 0:
        print("You are standing in front of a large door hewn from the rock face. There is a loose boulder above it.")
        print("It doesnt look very inviting.")
        print("\nNew options!\n")
        print("* Check HP.")
        print("* Push boulder.")
        print("Enter.")

    elif room == 1:
        print("You are in a well lit room.\nThere is a door ahead of you and on your left and right.\nThere is a strange pattern on the floor in the center of the room, it looks ominous.")
        print("\nNew options!\n")
        print("* Step around the middle.")
        print("* Step into the strange pattern.")
        print("Left.")
        print("Straight.") 
        print("Right.")
        print("Check HP.")
        print("Leave.")
    
    elif room == 2:
        print("You are in a large room. It is dimly lit by a crack in the\nceiling that is letting some sunlight in through the trees above.\nYou see an imp in front of you, it seems to have been approaching")
        print("since you entered the room.\n\nRoots of the trees are poking through the roof, it looks like you\ncould break one off to defend yourself.")
        print("\nNew options!\n")      
        print("* Move away from the imp.")
        print("* Grab a root.")
        print("Check HP.")
        print("Leave.")
    
    elif room == 3:
        print("On your left you see a large purple jar, it's billowing smoke.")
        print("On the ground beside the jar, you see an ornate cork.")
        print("In the center of the room swirls a pile of bones, a skeleton looks to be forming in the\nmiddle.")
        print("\nNew options!\n")      
        print("* Kick over the jar.")
        print("* Plug the jar.")
        print("* Try and disrupt the bones.")
        print("Check HP.")
        print("Leave.")

    elif room == 4:
        print("The walls of the room are bare, all that you can see is your shadow reflecting off the walls.")
        print("You search for an exit for a few hours, but come up with nothing. As you are about to give up")
        print("hope, you notice that your shadow isn't exactly mirroring your actions.\n")
        print("The shadow stops moving completely and appears to grow darker. The wall almost looks like it's\ncovered in ink.")
        print("First a ripple forms on the surface, then suddenly a pitch black mirror image of yourself\npushes itself away from the wall and lunges at you.")
        print("\nNew options!\n")      
        print("* Back up.")
        print("* Put out your light.")
        print("Check HP.")
        print("Leave.")

    # Prints the bottom border of look
    border()

def hpChange(change):
    # Imports HP variable into function
    global hp

    hp = hp + change

    # Kills if hp goes below 0
    if hp <= 0:
        return dead("You ran out of HP!")

def Continue(dead):
    global hp, skeleTreasure

    print("Do you want to start again?\n")
    border()
    Continue = input("> ").lower()

    if "y" in Continue and dead == True:
        hp = 20
        skeleTreasure = False
        return start()
    elif "y" in Continue and dead == False:
        return start()
    else:
        exit(0)

def dead(why):

    if why == "skeleKick":
        print("Your flesh gets ripped from your bones, as your rise against your will as an animated skeleton.\n")
        return Continue(True)
    
    elif why == "skeleTime":
        print("The smoke from the jar now completely fills the room, you start choking on the thick fog.\nBefore you lose conciousness, you see a shadowy figure approach, cackling in the same voice that was counting down.")
        return Continue(True)

    else:
        print(why, "You died.")
        return Continue(True)

def leave(progress):
    # Import global variables
    global hp, skeleTreasure

    if progress == "boulder":
        print("You push the boulder and it blocks the entrance!\n")
        print("Your curiosity got the best of you and you sealed the cave forever.\n")

    elif progress == "skeleTreasure":
        print("You get the skeleton's treasure!")
        print("You have", hp, "hp remaining, do you try your luck and re-enter the cave?\n")
        skeleTreasure = True
    
    else:
        print("You get spooked and go home, but at least you got to see", progress)
        print("You have", hp, "hp remaining, you coward!\n")
    
    return Continue(False)

def jar(state):
    if state == "kicked":
        print("\nYou kick the jar over - it shatters! Smoke starts to come out even faster.\n")
        print("You see your life flash before your eyes on the reflection of the shards as dozens of skeletons\nappear.\n")
        return dead("skeleKick")
    elif state == "corked":
        print("\nYou plug the jar with the ornate cork.")
        print("The smoke stops coming out of the jar. The unfinished skeleton in the center of the room crawls\ntowards you.")
        print("You're easily able to rekt the skeleton and it collapses to the floor.")
        return leave("skeleTreasure")
    elif state == "time":
        return dead("skeleTime")

def start():
    # Import Global Variables
    global leaveRoom
    looked = False
    leaveRoom = False
    leek = False

    border()
    print("Welcome to the cave of decisions.")
    print("Will you enter the cave?")
    print("\nNew Options!\n")
    print("* Look.")
    print("* Enter.")
    border()

    while leaveRoom == False:

        choice = input("> ").lower()

        if "look" in choice and looked == True:
            print("You've already looked around.")
        elif choice == "look" and looked == False:
            look(0)
            looked = True    
        elif "boulder" in choice and looked == True:
            return leave("boulder")
        elif choice == "enter":
            if leek == True:
                return roomTrap(True)
            else:
                return roomTrap(False)
        elif "leave" in choice:
            return leave("the front door.")              
        elif "check" in choice:
            print("You have", hp, "HP remaining")
        elif "console" in choice:
            break
        elif choice == "leek" and leek == False:
            leek = True
        elif choice == "leek" and leek == True:
            print("You have a leek.")
        else:
            print("I don't know what you're trying to do.")

def roomTrap(leek):
    # Sets Variables
    global leaveRoom
    
    leaveRoom = True
    leaveRoom = False
    looked = False
    trap = True

    border()
    print("You enter the cave.")
    print("There are three ways before you.")
    print("What do you do?")
    print("\nNew Options!\n")
    print("* Look")
    print("* Left.")
    print("* Right.")
    print("* Straight.") 
    print("Check HP.")
    print("Leave.")
    border()


    while leaveRoom == False:

        choice = input("> ").lower()
        
        if looked == True and "look" in choice:
            print("You have already looked around.\n")
        elif looked == True and "into" in choice:
            dead("You the floor gives away and you are impaled on spikes 20 feet below.")
        elif looked == True and "around" in choice:
            print("You step around the strange pattern, do you go Left, Right, or Straight?\n")
            trap = False

        elif looked == False and "look" in choice:    
            look(1)
            looked = True              

                
        elif "left" in choice and trap == True:
            dead("The floor gives away and you are impaled on spikes 20 feet below.")
        elif "left" in choice and trap == False:
            return roomImp()
        elif "right" in choice and trap == True:
            return dead("The floor gives away and you are impaled on spikes 20 feet below.")
        elif "right" in choice and trap == False:
            return roomSkele()
        elif "straight" in choice and trap == True:
            return dead("The floor gives away and you are impaled on spikes 20 feet below.")    
        elif "straight" in choice and trap == False:
            if leek == True:
                return roomBoss(2)
            else:
                return roomBoss(0)

        elif "leave" in choice:
            return leave("the inside.")

        # Check your hp    
        elif "check" in choice:
            print("You have", hp, "HP remaining\n")

        else:
            print("I don't know what you mean.")  

def roomImp():
    # Set Variables
    global leaveRoom

    leaveRoom = True
    leaveRoom = False
    looked = False
    stick = False
    imp = False
    approach = 4

    def impCheck():
        # Returns true to see if you can see the imp
        if approach >= 10:
            return True
        else:
            return False

    def impDistance():
        # Prints how far away the imp is
        if approach == 9:
            print("The imp is", 10 - approach, "meter away from you!\n") 
        else:
            print("The imp is", 10 - approach, "meters away from you.\n")

    border()
    print("You enter a very large room.")
    print("The sound of splashing water echoes faintly in the distance.")
    print("\nNew Options!\n")
    print("* Look.")
    print("* Move towards the sound.")
    print("Check HP.")
    print("Leave.")
    border()
    

    while leaveRoom == False:

        approach += 2

        choice = input("> ").lower()
        
        # You have the power
        if stick == True and impCheck() == True:
            border()
            print("The imp lunges at you!\n")
            print("You jab at it with the root and you connect with it's jaw, it recoils in pain.")
            print("The imp gets scared and flees through the crack in the ceiling!")
            print("\nYou are able to create a torch out of the root, and venture deeper into the cave. \nYou come across a door and enter it.")
            border()
            return roomBoss(1)

        # Stuff post looking
        elif looked == True and "look" in choice:
            print("You have already looked around")
            impDistance()  
        elif looked == True and "check" in choice:
            print("You have", hp, "HP remaining.")
            impDistance()
        elif looked == True and "leave" in choice:
            return leave("the imp.")       
        elif looked == True and "move" in choice:
            if imp == True and impCheck() == True:
                print("The imp is too close now!\n")
            elif imp == True and impCheck() == False:
                approach += -1
                print("You scramble away from the imp, but its moving too fast to escape from.\n")
                impDistance()
        # required for combat
        elif looked == True and "root" in choice:
            stick = True
            print("You grab an old, dry root, looks like you can use it as a spear.\n")
        elif looked == True and impCheck() == False:
            impDistance()


        # Pre looking
        elif looked == False and "check" in choice:
            print("You have", hp, "HP remaining.\n")
        elif looked == False and impCheck() == True and imp == False:
            print("An imp appears in front of you!")
            imp = True
        elif looked == False and "look" in choice:
            look(2)
            looked = True
            imp = True
            impDistance()
        elif looked == False and impCheck() == False and "move" in choice:
                approach += 1
                border()
                print("You move further into the room, staring at the ceiling.")
                print("The splashing shound gets louder, it sounds like footsteps.\n")
                border()
        elif looked == False and "leave" in choice:
            if imp == True:
                return leave("the imp and got scratched.")
            else:
                return leave("through an obvious trap.")   
        # You do not have the power
        elif stick == False and impCheck() == True:
            # Prevents imp from going inside you
            approach = 10
            print("The imp is right in front of you!")
            print("It swings at you and draws blood, you lose 5 HP!\n")
            hpChange(-5)

        else:
            print("I don't know what you're trying to do.") 

def roomSkele():
    # Set Variables
    global leaveRoom
    looked = False
    timeLeft = 3
    leaveRoom = True
    leaveRoom = False

    border()
    print("On the right side of the room there is a fissure that splits the cave in two, barely large enough\nfor you to fit through. You have to take your armor off in order to squeeze through the gap.")
    print("As you reach the other side, you hear a swirling rattle.")

    print("\nNew Options!\n")
    print("* Look.")
    print("Check HP.")
    print("Leave.")
    border()

    while leaveRoom == False:

        if timeLeft == 0:
            print("The voice calls out: Your time is up...\n")
            return jar("time")
        elif timeLeft >= 0: 
            print("\nA ghastly voice calls out: ", timeLeft)
            print("The thick smoke is suffocating, you lose 5 hp!")
            hpChange(-5)   

        choice = input("> ").lower()

        if "check" in choice:
            print("You have", hp, "HP remaining\n")

        elif looked == True and "look" in choice:
            print("You have already looked around")
        elif looked == True and "leave" in choice:
            leave("the magic jar.")
        elif looked == True and "kick" in choice:
            jar("kicked")
        elif looked == True and "plug" in choice:
            jar("corked")
        elif looked == True and "bones" in choice:
            print("You can't pull the bones from the skeleton fast enough, it keep building up.")
        elif looked == True and "consume" in choice:
            print("You eat the bones, but they keep forming faster than you can keep up.")
        

        elif looked == False and "look" in choice:
            look(3)
            looked = True 
        elif looked == False and "leave" in choice:
            return leave("through an obvious trap.")   

        else:
            print("I don't know what you're trying to do.")

        timeLeft += -1
        time.sleep(1)

def roomBoss(stick):
    global hp, skeleTreasure, leaveRoom
    looked = False
    leaveRoom = True
    leaveRoom = False

    border()
    print("You step into a tiny room. The door slams behind you.")

    if stick == 0:
        print("It's completely dark, you can't see anything!")
        return dead("You wander around in the dark until you starve.")
    elif stick == 1:
        print("The torch you crafted in the previous room comes in handy, this room would be pitch black without it.")
    elif stick == 2:
        print("The leek you picked up outside begins resonating and illuminates the room!")

    print("\nNew Options!\n")
    print("* Look.")
    print("Check.")
    print("Leave.")
    border()

    while leaveRoom == False:
    
        choice = input("> ").lower()

        if "check" in choice:
            print("You have", hp, "HP remaining\n")        
        elif "leave" in choice:
            print("The door is locked from the other side, you can't leave!")

        elif looked == True and "look" in choice:
            print("You've already looked around!")
        elif looked == True and "back" in choice:
            print("You try and back up, but the room is small and there's nowhere to go, the shadow reaches out and grabs you.")
            hpChange(-10)
            print("The shadow does 10 HP worth of damage, you only have", hp, "remaining!")
        elif looked == True and "out" in choice:
            border()
            if stick == 2:
                print("You put out your leek!\n")
            else:
                print("You put out your torch!\n")
            print("\"Hey, I can't see anything!\" cries a voice, clearly distressed.")
            print("\"I want to get out of here, I'm scared!\". The shadow creature begins yelling in an undecipherable dialect and pounding on the walls.\nIn the total darkness you can only cower and cover your head as the ceiling begins to collapse, after a few tense moments, the pounding stops and you are blinded by a\nbrilliant glow - it's the outside! You survived!")
            border()
        elif looked == False and "look" in choice:
            look(4)
            looked = True
        else:
            print("I don't know what youre trying to do.")

start()

