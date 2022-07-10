class Character:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.speed = 0
        self.strength = 0
        self.magic = 0
        self.intelligence = 0

    def get_speed_score(self):
        return self.speed

    def set_speed_score(self, score):
        self.speed = score

    def get_strength_score(self):
        return self.strength

    def set_strength_score(self, score):
        self.strength = score

    def get_magic_score(self):
        return self.magic

    def set_magic_score(self, score):
        self.magic = score

    def get_intelligence_score(self):
        return self.magic

    def set_intelligence_score(self, score):
        self.intelligence = score

    def get_overall_score(self):
        overall_score = (self.speed + self.strength + self.magic + self.intelligence) / 4
        return overall_score


import random

rows = 6  # Pattern(1,121,12321,1234321,123454321)
for i in range(1, rows + 1):
    for j in range(1, i - 1):
        print('##', end=" ")
    for j in range(i - 1, 0, -1):
        print('##', end=" ")
    print()
print('Hello')
status = input('When you want to stop making characters click on "2" otherwise give me a "1"')
heroes = []
villains = []
while status != '2':
    name = input('what is the character\'s name? ')
    type = input('what is their type (hero or villain)')
    c = Character(name, type)
    speed = int(input('what is their speed score (1-10)'))
    c.set_speed_score(speed)
    strength = int(input('what is their strength score (1-10)'))
    c.set_strength_score(strength)
    magic = int(input('what is their magic score (1-10)'))
    c.set_magic_score(magic)
    intelligence = int(input('what is their intelligence score (1-10)'))
    c.set_intelligence_score(intelligence)
    if c.type == 'hero':
        heroes.append(c)
    elif c.type == 'villain':
        villains.append(c)
    status = input('When you want to stop making characters click on "2" otherwise give me a "1"')
h = random.choice(heroes)
v = random.choice(villains)

print('The fight is between ' + h.name + ' and ' + v.name)
if h.get_overall_score() >= v.get_overall_score():
    print('Yay! ' + h.name + ' wins!!')
else:
    print('Oh No! ' + v.name + ' wins!!')
    print('Run!!')
