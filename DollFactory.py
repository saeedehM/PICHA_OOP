class ToyFactory:
    def __init__(self, color, name, material):
        self.color = color
        self.name = name
        self.material = material
    def dance(self):
        print("I am dancing")
    def roll(self):
        print("I am rolling")
    def talk(self):
        print("I am talking")
    def walk(self):
        print("I am walking")
class Animals(ToyFactory):
    def __init__(self, color, name, material):
        super.__init__(color, name, material)
        self.fluffy = True
    def walk(self):
        print("I am walking on paws")
    def fight(self):
        print("I am fighting")
class Dog(Animals):
    def talk(self):
        print("Bark Bark")
