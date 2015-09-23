from sys import exit
from random import randint
from time import sleep


class Scene(object):

    ammo = 10
    game_over = True
    knife = False
    note = False
    key = False
    rooms = {}
    evaded = {}

    def enter(self):
        print "This scene is not conifgured. Subclass it and implement enter()."

    def print_dash(self):
        print "ammo: %d\t\t\t\thelp: commands" % self.ammo
        print "--------------------------------------------------------\n"

    def print_dashz(self, zombies):
        print "zombies: %d\t\t\t\thelp: commands" % zombies
        print "--------------------------------------------------------\n"

    def print_room_commands(self):
        print ""
        print "search room  -   Search room for usable items."
        print "leave room   -   Leave current room."
        print "view items   -   View items inventory."
        if self.note == True:
            print "use note     -   Use post-it note."
        if self.key == True:
            print "use key      -   Use strangely shaped key."
        print "help         -   Print available commands."
        print "quit         -   Quit the game."

    def print_attack_commands(self):
        print ""
        if self.knife == True:
            print "use knife    -   Use your knife."
        print "shoot pistol -   Fire your pistol."
        print "evade        -   Evade by pushing your way through."
        print "help         -   Print available commands.\n"

class Death(Scene):

    def enter(self):
        print "You scream in terror as you hear and feel the tearing of your flesh...not a good time."
        print "GAME OVER!"
        raw_input("Press Enter to continue...")
        Scene.rooms = {}
        Scene.evaded = {}
        Scene.game_over = True
        return 'grand_foyer'

class GrandFoyer(Scene):

    def enter(self):
        print "You're in the GRAND FOYER...\n"
        super(GrandFoyer, self).print_dash()
        
        if "grand foyer" not in Scene.rooms:
            Scene.rooms["grand foyer"] = 0

        print "What would you like to do?"
        action = raw_input("> ")
        action = action.lower()

        if action == "search room":
            print "\nThere are no items of importance in this room."
            raw_input("Press Enter to continue...")
            return 'grand_foyer'
        elif action == "leave room":
            
            while True:
                print "\nWhere do you want to go?"
                print "------------------------"
                print "dining room"
                print "stair case"
                print "study\n"
                print "cancel\n"
                room = raw_input("> ")
                room = room.lower()

                if room == "dining room":
                    return 'dining_room'
                elif room == "stair case":
                    return 'stair_case'
                elif room == "study":
                    return 'study'
                elif room == "cancel":
                    return 'grand_foyer'
                else:
                    print "\n%s is not a valid room.\n" % room

        elif action == "view items":
            return 'grand_foyer'
        elif action == "help":
            super(GrandFoyer, self).print_room_commands()
            return 'grand_foyer'
        elif action == "quit":
            exit(1)
        else:
            print "\n%s is not a valid command." % action
            return 'grand_foyer'

class DiningRoom(Scene):

    def enter(self):
        print "You're in the DINING ROOM...\n"
        super(DiningRoom, self).print_dash()

        if "dining room" not in Scene.rooms:
            zombies = randint(1, 2)
            Scene.rooms["dining room"] = zombies
            Scene.evaded["dining room"] = False
            evaded = Scene.evaded["dining room"]
        else:
            zombies = Scene.rooms["dining room"]
            evaded = Scene.evaded["dining room"]

        if zombies > 1 and evaded == False:
            
            if Scene.game_over == True:
                print "As you enter the room, you're greeted by a terrible sight."
                print "%d zombies notice you and start to tread your way very slowly." % zombies
                print "Their grotesque appearances leave you in shock,"
                print "and you struggle to decide what to do."
                raw_input("Press Enter to continue...")
                Scene.game_over = False
            else:
                print "THERE ARE %d ZOMBIES HERE!!!" % zombies

        elif zombies == 1 and evaded == False:

            if Scene.game_over == True:
                print "As you enter the room, you're greeted by a terrible sight."
                print "%d zombie notices you and starts to tread your way very slowly." % zombies
                print "Its grotesque appearance leaves you in shock,"
                print "and you struggle to decide what to do."
                raw_input("Press Enter to continue...")
                Scene.game_over = False
            else:
                print "THERE IS %d ZOMBIE HERE!!!" % zombies
                
        while zombies != 0 and evaded == False:
            super(DiningRoom, self).print_dashz(zombies)
            print "What would you like to do?"
            action = raw_input("> ")
            action = action.lower()

            if action == "use knife" and knife == True:
                killed = randint(1, zombies)
                print "Using your knife, you try to slash your way through."
                raw_input("Press Enter to continue...")

                if killed > 1:
                    print "You managed to kill %d zombies!" % killed
                    zombies = zombies - killed
                else:
                    print "You managed to kill %d zombie!" % killed
                    zombies = zombies - killed

                if zombies > 1:
                    print "%d zombies remain." % zombies
                else:
                    print "%d zombie remains." % zombies

                Scene.rooms["dining room"] = zombies
                raw_input("Press Enter to continue...")

            elif action == "shoot pistol":
                killed = randint(0, zombies)
                print "You pull out your pistol with lightning speed and fire, aiming for head shots."
                raw_input("Press Enter to continue...")

                if killed > 1:
                    print "You managed to kill %d zombies!" % killed
                    Scene.ammo = Scene.ammo - zombies
                    zombies = zombies - killed
                elif killed == 1:
                    print "You managed to kill %d zombie!" % killed
                    Scene.ammo = Scene.ammo - zombies
                    zombies = zombies - killed
                else:
                    print "All your shots missed!"
                    Scene.ammo = Scene.ammo - zombies

                if zombies > 1:
                    print "%d zombies remain." % zombies
                else:
                    print "%d zombie remains." % zombies

                Scene.rooms["dining room"] = zombies
                raw_input("Press Enter to continue...")

            elif action == "evade":
                        
                if zombies > 1:
                    print "You decide to try your luck and dodge the %d zombies." % zombies
                    successful = randint(0, 1)
                    raw_input("Press Enter to continue...")

                    if successful == 1:
                        print "You were able to successfully dodge the zombies."
                        print "In their clumsy attempt to grab you, they topple over each other."
                        print "Even though they attempt to get back up,"
                        print "they are slow enough to allow you to decide what to do next."
                        raw_input("Press Enter to continue...")
                        evaded = True
                        Scene.evaded["dining room"] = evaded
                    else:
                        print "As you try to make your way through, you are overwhelmed."
                        return 'death'
                
                else:
                    print "You decide to try your luck and dodge the %d zombie." % zombies
                    raw_input("Press Enter to continue...")
                    print "you were able to successfully dodge the zombie."
                    print "In its clumsy attempt to grab you, it topples to the floor."
                    print "Even though it attempts to get back up,"
                    print "it's slow enough to allow you to decide what to do next."
                    raw_input("Press Enter to continue...")
                    evaded = True
                    Scene.evaded["dining room"] = evaded

            elif action == "help":
                super(DiningRoom, self).print_attack_commands()
            else:
                print "\n%s is not a valid command.\n" % action

        print "What would you like to do?"
        action = raw_input("> ")
        action = action.lower()

        if action == "search room":
            print "\nThere are no items of importance in this room."
            raw_input("Press Enter to continue...")
            return 'dining_room'
        elif action == "leave room":
            while True:
                print "\nWhere do you want to go?"
                print "------------------------"
                print "kitchen"
                print "grand foyer\n"
                print "cancel\n"
                room = raw_input("> ")
                room = room.lower()

                if room == "kitchen":
                    evaded = False
                    Scene.evaded["dining room"] = evaded
                    return 'kitchen'
                elif room == "grand foyer":
                    evaded = False
                    Scene.evaded["dining room"] = evaded
                    return 'grand_foyer'
                elif room == "cancel":
                    return 'dining_room'
                else:
                    print "\n%s is not a valid room.\n" % room

        elif action == "view items":
            return 'dining_room'
        elif action == "help":
            super(DiningRoom, self).print_room_commands()
            return 'dining_room'
        elif action == "quit":
            exit(1)
        else:
            print "\n%s is not a valid command." % action
            return 'dining_room'

class Kitchen(Scene):

    def enter(self):
        print "You're in the KITCHEN...\n"
        super(Kitchen, self).print_dash()
        print "What would you like to do?"
        action = raw_input("> ")
        action = action.lower()

        if action == "search room":
            print "\nThere are no items of importance in this room."
            raw_input("Press Enter to continue...")
            return 'kitchen'
        elif action == "leave room":
            while True:
                print "\nWhere do you want to go?"
                print "------------------------"
                print "dining room\n"
                print "cancel\n"
                room = raw_input("> ")
                room = room.lower()

                if room == "dining room":
                    return 'dining_room'
                elif room == "cancel":
                    return 'kitchen'
                else:
                    print "\n%s is not a valid room.\n" % room

        elif action == "view items":
            return 'kitchen'
        elif action == "help":
            super(Kitchen, self).print_room_commands()
            return 'kitchen'
        elif action == "quit":
            exit(1)
        else:
            print "\n%s is not a valid command." % action
            return 'kitchen'

class Study(Scene):

    def enter(self):
        print "You're in the STUDY...\n"
        super(Study, self).print_dash()
        print "What would you like to do?"
        action = raw_input("> ")
        action = action.lower()

        if action == "search room":
            print "\nThere are no items of importance in this room."
            raw_input("Press Enter to continue...")
            return 'study'
        elif action == "leave room":
            while True:
                print "\nWhere do you want to go?"
                print "------------------------"
                print "back patio"
                print "grand foyer\n"
                print "cancel\n"
                room = raw_input("> ")
                room = room.lower()

                if room == "back patio":
                    return 'back_patio'
                elif room == "grand foyer":
                    return 'grand_foyer'
                elif room == "cancel":
                    return 'grand_foyer'
                else:
                    print "\n%s is not a valid room.\n" % room

        elif action == "view items":
            return 'study'
        elif action == "help":
            super(Study, self).print_room_commands()
            return 'study'
        elif action == "quit":
            exit(1)
        else:
            print "\n%s is not a valid command." % action
            return 'study'

class BackPatio(Scene):

    def enter(self):
        print "You're in the BACK PATIO...\n"
        super(BackPatio, self).print_dash()
        print "What would you like to do?"
        action = raw_input("> ")
        action = action.lower()

        if action == "search room":
            print "\nThere are no items of importance in this room."
            raw_input("Press Enter to continue...")
            return 'back_patio'
        elif action == "leave room":
            while True:
                print "\nWhere do you want to go?"
                print "------------------------"
                print "study\n"
                print "cancel\n"
                room = raw_input("> ")
                room = room.lower()

                if room == "study":
                    return 'study'
                elif room == "cancel":
                    return 'back_patio'
                else:
                    print "\n%s is not a valid room.\n" % room

        elif action == "view items":
            return 'back_patio'
        elif action == "help":
            super(BackPatio, self).print_room_commands()
            return 'back_patio'
        elif action == "quit":
            exit(1)
        else:
            print "\n%s is not a valid command." % action
            return 'back_patio'

class StairCase(Scene):

    def enter(self):
        print "You're in the STAIR CASE...\n"
        super(StairCase, self).print_dash()
        print "What would you like to do?"
        action = raw_input("> ")
        action = action.lower()

        if action == "search room":
            print "\nThere are no items of importance in this room."
            raw_input("Press Enter to continue...")
            return 'stair_case'
        elif action == "leave room":
            while True:
                print "\nWhere do you want to go?"
                print "------------------------"
                print "hallway"
                print "grand foyer\n"
                print "cancel\n"
                room = raw_input("> ")
                room = room.lower()

                if room == "hallway":
                    return 'hallway'
                elif room == "grand foyer":
                    return 'grand_foyer'
                elif room == "cancel":
                    return 'stair_case'
                else:
                    print "\n%s is not a valid room.\n" % room

        elif action == "view items":
            return 'stair_case'
        elif action == "help":
            super(StairCase, self).print_room_commands()
            return 'stair_case'
        elif action == "quit":
            exit(1)
        else:
            print "\n%s is not a valid command." % action
            return 'stair_case'

class Hallway(Scene):

    def enter(self):
        print "You're in the HALLWAY...\n"
        super(Hallway, self).print_dash()
        print "What would you like to do?"
        action = raw_input("> ")
        action = action.lower()

        if action == "search room":
            print "\nThere are no items of importance in this room."
            raw_input("Press Enter to continue...")
            return 'hallway'
        elif action == "leave room":
            while True:
                print "\nWhere do you want to go?"
                print "------------------------"
                print "bedroom"
                print "bathroom"
                print "master bedroom"
                print "stair case\n"
                print "cancel\n"
                room = raw_input("> ")
                room = room.lower()

                if room == "bedroom":
                    return 'bedroom'
                elif room == "bathroom":
                    return 'bathroom'
                elif room == "master bedroom":
                    return 'master_bedroom'
                elif room == "stair case":
                    return 'stair_case'
                elif room == "cancel":
                    return 'hallway'
                else:
                    print "\n%s is not a valid room.\n" % room

        elif action == "view items":
            return 'hallway'
        elif action == "help":
            super(Hallway, self).print_room_commands()
            return 'hallway'
        elif action == "quit":
            exit(1)
        else:
            print "\n%s is not a valid command." % action
            return 'hallway'

class Bedroom(Scene):

    def enter(self):
        print "You're in the BEDROOM...\n"
        super(Bedroom, self).print_dash()
        print "What would you like to do?"
        action = raw_input("> ")
        action = action.lower()

        if action == "search room":
            print "\nThere are no items of importance in this room."
            raw_input("Press Enter to continue...")
            return 'bedroom'
        elif action == "leave room":
            while True:
                print "\nWhere do you want to go?"
                print "------------------------"
                print "hallway\n"
                print "cancel\n"
                room = raw_input("> ")
                room = room.lower()

                if room == "hallway":
                    return 'hallway'
                elif room == "cancel":
                    return 'bedroom'
                else:
                    print "\n%s is not a valid room.\n" % room

        elif action == "view items":
            return 'bedroom'
        elif action == "help":
            super(Bedroom, self).print_room_commands()
            return 'bedroom'
        elif action == "quit":
            exit(1)
        else:
            print "\n%s is not a valid command." % action
            return 'bedroom'

class Bathroom(Scene):

    def enter(self):
        print "You're in the BATHROOM...\n"
        super(Bathroom, self).print_dash()
        print "What would you like to do?"
        action = raw_input("> ")
        action = action.lower()

        if action == "search room":
            print "\nThere are no items of importance in this room."
            raw_input("Press Enter to continue...")
            return 'bathroom'
        elif action == "leave room":
            while True:
                print "\nWhere do you want to go?"
                print "------------------------"
                print "hallway\n"
                print "cancel\n"
                room = raw_input("> ")
                room = room.lower()

                if room == "hallway":
                    return 'hallway'
                elif room == "cancel":
                    return 'bathroom'
                else:
                    print "\n%s is not a valid room.\n" % room

        elif action == "view items":
            return 'bathroom'
        elif action == "help":
            super(Bathroom, self).print_room_commands()
            return 'bathroom'
        elif action == "quit":
            exit(1)
        else:
            print "\n%s is not a valid command." % action
            return 'bathroom'

class MasterBedroom(Scene):

    def enter(self):
        print "You're in the MASTER BEDROOM...\n"
        super(MasterBedroom, self).print_dash()
        print "What would you like to do?"
        action = raw_input("> ")
        action = action.lower()

        if action == "search room":
            print "\nThere are no items of importance in this room."
            raw_input("Press Enter to continue...")
            return 'master_bedroom'
        elif action == "leave room":
            while True:
                print "\nWhere do you want to go?"
                print "------------------------"
                print "terrace"
                print "hallway\n"
                print "cancel\n"
                room = raw_input("> ")
                room = room.lower()

                if room == "terrace":
                    return 'terrace'
                elif room == "hallway":
                    return 'hallway'
                elif room == "cancel":
                    return 'master_bedroom'
                else:
                    print "\n%s is not a valid room.\n" % room

        elif action == "view items":
            return 'master_bedroom'
        elif action == "help":
            super(MasterBedroom, self).print_room_commands()
            return 'master_bedroom'
        elif action == "quit":
            exit(1)
        else:
            print "\n%s is not a valid command." % action
            return 'master_bedroom'

class Terrace(Scene):

    def enter(self):
        print "You're in the TERRACE...\n"
        super(Terrace, self).print_dash()
        print "What would you like to do?"
        action = raw_input("> ")
        action = action.lower()

        if action == "search room":
            print "\nThere are no items of importance in this room."
            raw_input("Press Enter to continue...")
            return 'terrace'
        elif action == "leave room":
            while True:
                print "\nWhere do you want to go?"
                print "------------------------"
                print "master bedroom\n"
                print "cancel\n"
                room = raw_input("> ")
                room = room.lower()

                if room == "master bedroom":
                    return 'master_bedroom'
                elif room == "cancel":
                    return 'terrace'
                else:
                    print "\n%s is not a valid room.\n" % room

        elif action == "view items":
            return 'terrace'
        elif action == "help":
            super(Terrace, self).print_room_commands()
            return 'terrace'
        elif action == "quit":
            exit(1)
        else:
            print "\n%s is not a valid command." % action
            return 'terrace'

class Ending(Scene):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        print "\nZombie Nightmare"
        print "----------------\n\n"
        print "You are a detective investigating strange disappearances"
        print "and you received a possible lead, directing you towards an"
        print "old abandoned mansion."
        print "As you approach the property, you hear strange growling"
        print "coming from both sides of you."
        print "The overgrown grass prevents you" 
        print "from seeing what these creatures are,"
        print "so you run as fast as you can"
        print "towards the mansion since it's closer to you."
        print "In haste, you open the unlocked door and enter," 
        print "slamming it shut behind you."
        print "Armed with only a pistol, you believe you're safe"
        raw_input("Press Enter to continue...")
        print "...for now."
        sleep(2)
        
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n--------------------------------------------------------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Map(object):

    scenes = {
        'grand_foyer': GrandFoyer(),
        'dining_room': DiningRoom(),
        'kitchen': Kitchen(),
        'study': Study(),
        'back_patio': BackPatio(),
        'stair_case': StairCase(),
        'hallway': Hallway(),
        'bedroom': Bedroom(),
        'bathroom': Bathroom(),
        'master_bedroom': MasterBedroom(),
        'terrace': Terrace(),
        'death': Death(),
        'ending': Ending()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

