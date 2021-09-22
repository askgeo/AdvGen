import random
import die
import world


class Adventurer:
    """Outer Class"""

    def __init__(self, name):

        # Basic traits.
        self.name = name
        self.age = random.randint(12,62)

        # Gender.
        self.gender = random.choice(list(world.genderDict))

        # Race.
        self.race = random.choice(world.traitDict['races'])

        # Personal traits.
        self.alignment = random.choice(world.traitDict['alignments'])
        self.personality = random.choice(world.traitDict['personalities'])
        self.hobby = random.choice(world.traitDict['hobbies'])

        # Character stats.
        self.str = die.rollstats()
        self.con = die.rollstats()
        self.dex = die.rollstats()
        self.wis = die.rollstats()
        self.int = die.rollstats()
        self.cha = die.rollstats()

        # Character class and features.
        self.pclass = random.choice(list(world.wizardDict))

    # A method for listing Adventurer attributes
    def attributes(self):
        print(
            f'ATTRIBUTES:\n',
            f'Name: {self.name} \n',
            f'Age: {self.age} \n',
            f'Gender: {self.gender} \n',
            f'Race: {self.race} \n',
            f'Class: Wizard \n',
            f'Alignment: {self.alignment} \n',
            f"\n --------------------------- \n",
        )

    # A method for describing the Adventurer
    def narrative(self):
        print(
            f"DESCRIPTION: \n",
            f"{self.name} is a {self.personality} amateur {self.hobby}. \n",
            f"\n --------------------------- \n",
        )

    # A method for calling a stat block.
    def stats(self):
        print(
            f'STATS:\n',
            f'STR: {self.str} \n',
            f'DEX: {self.dex} \n',
            f'CON: {self.con} \n',
            f'WIS: {self.wis} \n',
            f'INT: {self.int} \n',
            f'CHA: {self.cha} \n',
            f"\n --------------------------- \n",
        )

# Start program
p1 = Adventurer("Tom")
p1.attributes()
p1.narrative()
p1.stats()