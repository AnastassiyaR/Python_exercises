"""Spaceship."""


class Crewmate:
    """Crewmate class."""

    def __init__(self, color: str, role: str, tasks: int = 10):
        """
        Initialize player class.

        :param color: The color of the crewmate.
        :param role: The role of the crewmate.
        :param color: The tasks of the crewmate.
        :param protected: If the tasks are protected or not.
        """
        roles = ["Crewmate", "Sheriff", "Guardian Angel", "Altruist"]
        if role.title() in roles:
            self.role = role.title()
        else:
            self.role = "Crewmate"

        self.color = color.title()
        self.tasks = int(tasks)
        self.protected = False

    def color(self):
        """Return the color of the crewmate."""
        return self.color

    def role(self):
        """Return the role of the crewmate."""
        return self.role

    def tasks(self):
        """Return the tasks of the crewmate."""
        return self.tasks

    def __repr__(self):
        """
        Represent crewmate information.

        Format the string of the crewmate information as:
        '[color], role: [role], tasks left: [tasks]'
        """
        return f"{self.color}, role: {self.role}, tasks left: {self.tasks}."

    def complete_task(self):
        """Remove the 1 point from the number of tasks are left."""
        if self.tasks > 0:
            self.tasks -= 1


class Impostor:
    """Imposter class."""

    def __init__(self, color: str):
        """
        Initialize player class.

        :param color: The color of the imposter.
        :param kills: The kills of the imposter.
        """
        self.color = color
        self.kills = 0
        self.role = "Impostor"

    def color(self):
        """
        Return the color of the imposter.

        :param color: The color name, sorted by the first letter.
        """
        return self.color.title()

    def __repr__(self):
        """
        Represent impostor information.

        Format the string of the impostor information as:
        'Impostor [color], kills: [kills]'
        """
        return f"Impostor {self.color.title()}, kills: {self.kills}."


class Spaceship:
    """Spaceship class."""

    def __init__(self):
        """
        Initialize Spaceship class.

        :param dead_players: The dead players.
        :param crewmates: The crewmates' information.
        :param impostors: The impostors' information.
        """
        self.dead_players = []
        self.crewmates = []
        self.impostors = []

    def get_crewmate_list(self):
        """Get the list of crewmates."""
        return self.crewmates

    def get_impostor_list(self):
        """Get the list of impostors."""
        return self.impostors

    def add_crewmate(self, crewmate: Crewmate):
        """Add the crewmate in the crewmates' list."""
        if not any(crewmates.color == crewmate.color for crewmates in self.crewmates) and \
                not any(impostors.color == crewmate.color for impostors in self.impostors) and \
                crewmate.role.title() != "Impostor":
            self.crewmates.append(crewmate)

    def get_dead_players(self):
        """Get the list of the dead players."""
        return self.dead_players

    def add_impostor(self, impostor: Impostor):
        """Add the impostor in the impostors' list."""
        if not any(crewmates.color == impostor.color for crewmates in self.crewmates) and \
                not any(impostors.color == impostor.color for impostors in self.impostors) \
                and impostor.role == "Impostor" and len(self.impostors) < 3:
            self.impostors.append(impostor)

    def kill_impostor(self, sheriff: Crewmate, color: str):
        """Kill the impostor."""
        if sheriff.role == "Sheriff" and any(sheriff.color == person.color for person in self.crewmates):
            for impostor in self.impostors:
                if impostor.color.title() == color.title():
                    self.impostors.remove(impostor)
                    self.dead_players.append(impostor)
                    return True
            self.crewmates.remove(sheriff)
            self.dead_players.append(sheriff)

    def revive_crewmate(self, altruist: Crewmate, dead_crewmate: Crewmate):
        """Revive the crewmate the cost of the altruist."""
        if altruist.role == "Altruist" and \
                dead_crewmate in self.dead_players and altruist in self.crewmates:
            self.dead_players.remove(dead_crewmate)
            self.crewmates.append(dead_crewmate)
            self.crewmates.remove(altruist)
            self.dead_players.append(altruist)

    def protect_crewmate(self, guardian_angel: Crewmate, crewmate_to_protect: Crewmate):
        """Protect the crewmate."""
        if guardian_angel.role == "Guardian Angel" and guardian_angel in self.dead_players:
            if crewmate_to_protect in self.crewmates and not crewmate_to_protect.protected and \
                    not any(crewmate.protected for crewmate in self.crewmates):
                crewmate_to_protect.protected = True
                return True
        return False

    def kill_crewmate(self, impostor: Impostor, color: str):
        """Kill the crewmate."""
        if any(impostors.color == impostor.color for impostors in self.impostors):
            for crewmate in self.crewmates:
                if crewmate.color.title() == color.title():
                    if crewmate.protected:
                        crewmate.protected = False
                    else:
                        self.crewmates.remove(crewmate)
                        self.dead_players.append(crewmate)
                        impostor.kills += 1

    def sort_crewmates_by_tasks(self):
        """Sort the list of the crewmates by tasks."""
        return sorted(self.crewmates, key=lambda crewmate: crewmate.tasks)

    def sort_impostors_by_kills(self):
        """Sort the list of the impostors by kills."""
        return sorted(self.impostors, key=lambda impostor: impostor.kills, reverse=True)

    def get_regular_crewmates(self):
        """Return the list of regular crewmates."""
        return [crewmate for crewmate in self.crewmates if crewmate.role == "Crewmate"]

    def get_role_of_player(self, color: str):
        """Return the role of the given color."""
        all_players = self.crewmates + self.impostors
        for player in all_players:
            if player.color == color.title():
                return player.role
        return None

    def get_crewmate_with_most_tasks_done(self):
        """Return the crewmate with the most cost of done tasks."""
        return min(self.crewmates, key=lambda crewmate: crewmate.tasks)

    def get_impostor_with_most_kills(self):
        """Return the impostor with the most kills."""
        return max(self.impostors, key=lambda impostor: impostor.kills)


if __name__ == "__main__":
    print("Spaceship.")

    spaceship = Spaceship()
    print(spaceship.get_dead_players())  # -> []
    print()

    print("Let's add some crewmates.")
    red = Crewmate("Red", "Crewmate")
    white = Crewmate("White", "Impostor")
    yellow = Crewmate("Yellow", "Guardian Angel", tasks=5)
    green = Crewmate("green", "Altruist")
    blue = Crewmate("BLUE", "Sheriff", tasks=0)

    print(red)  # -> Red, role: Crewmate, tasks left: 10.
    print(white)  # -> White, role: Crewmate, tasks left: 10.
    print(yellow)  # -> Yellow, role: Guardian Angel, tasks left: 5.
    print(blue)  # -> Blue, role: Sheriff, tasks left: 0.
    print()

    print("Let's make Yellow complete a task.")
    yellow.complete_task()
    print(yellow)  # ->  Yellow, role: Guardian Angel, tasks left: 4.
    print()

    print("Adding crewmates to Spaceship:")
    spaceship.add_crewmate(red)
    spaceship.add_crewmate(white)
    spaceship.add_crewmate(yellow)
    spaceship.add_crewmate(green)
    print(spaceship.get_crewmate_list())  # -> [Red, role: Crewmate, tasks left: 10., White, role: Crewmate, tasks left: 10., Yellow, role: Guardian Angel, tasks left: 4., Green, role: Altruist, tasks left: 10.]

    spaceship.add_impostor(blue)  # Blue cannot be an Impostor.
    print(spaceship.get_impostor_list())  # -> []
    spaceship.add_crewmate(blue)
    print()

    print("Now let's add impostors.")
    orange = Impostor("orANge")
    black = Impostor("black")
    purple = Impostor("Purple")
    spaceship.add_impostor(orange)
    spaceship.add_impostor(black)

    spaceship.add_impostor(Impostor("Blue"))  # Blue player already exists in Spaceship.
    spaceship.add_impostor(purple)
    spaceship.add_impostor(Impostor("Pink"))  # No more than three impostors can be on Spaceship.
    print(spaceship.get_impostor_list())  # -> [Impostor Orange, kills: 0., Impostor Black, kills: 0., Impostor Purple, kills: 0.]
    print()

    print("The game has begun! Orange goes for the kill.")
    spaceship.kill_crewmate(orange, "yellow")
    print(orange)  # -> Impostor Orange, kills: 1.
    spaceship.kill_crewmate(black, "purple")  # You can't kill another Impostor, silly!
    print(spaceship.get_dead_players())  # -> [Yellow, role: Guardian Angel, tasks left: 4.]
    print()

    print("Yellow is a Guardian angel, and can protect their allies when dead.")
    spaceship.protect_crewmate(yellow, green)
    print(green.protected)  # -> True
    spaceship.kill_crewmate(orange, "green")
    print(green in spaceship.dead_players)  # -> False
    print(green.protected)  # -> False
    print()

    print("Green revives their ally.")
    spaceship.kill_crewmate(purple, "RED")
    spaceship.revive_crewmate(green, red)
    print(red in spaceship.dead_players)  # -> False
    print()

    print("Let's check if the sorting and filtering works correctly.")

    red.complete_task()
    print(spaceship.get_role_of_player("Blue"))  # -> Sheriff
    spaceship.kill_crewmate(purple, "blue")
    print(spaceship.sort_crewmates_by_tasks())  # -> [Red, role: Crewmate, tasks left: 9., White, role: Crewmate, tasks left: 10.]
    print(spaceship.sort_impostors_by_kills())  # -> [Impostor Purple, kills: 2., Impostor Orange, kills: 1., Impostor Black, kills: 0.]
    print(spaceship.get_regular_crewmates())  # -> [White, role: Crewmate, tasks left: 10., Red, role: Crewmate, tasks left: 9.]
