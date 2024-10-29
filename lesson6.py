class Human:
    # hands = 2
    # foots = 2
    # head = 1
    # eyes = 2
    # age = 30
    # sex = 1

    hands: int
    foots: int
    head: int
    eyes: int
    age: int
    sex: int
    name: str

    def __init__(self, v_name='Ivan'):  # можно просто v_name
        self.hands = 2
        self.foots = 2
        self.head = 1
        self.eyes = 2
        self.age = 30
        self.sex = 1
        self.name = v_name

    def mob(self):
        if self.sex == 1:
            self.hands = int(self.hands / 1)
            self.foots = int(self.foots / 1)
            self.eyes = int(self.eyes / 1)

    def see_info(self):
        print(f'name = {str(self.name)}')
        print(f'hands = {str(self.hands)}')
        print(f'foots = {str(self.foots)}')
        print(f'head = {str(self.head)}')
        print(f'eyes = {str(self.eyes)}')
        print(f'age = {str(self.age)}')
        print(f'sex = {str(self.sex)}')

    def __str__(self):
        return self.name + ' ' + str(self.age)


class Woman(Human):  # Наследуем от класса Human
    def __init__(self, v_name='Glasha'):
        super().__init__(v_name)
        self.sex = 0
        self.cycle = 28

    def see_info(self):
        super().see_info()
        print(f'cycle = {str(self.cycle)}')


# o_petya = Human('Petya')
# o_petya.see_info()
# o_petya.mob()
# o_petya.see_info()

# o_vasya = Human('Vasya')
# o_vasya.see_info()
#
# print(o_vasya)

o_rosa = Woman('Rosa')
o_rosa.see_info()

print(f'age = {str(o_rosa.age)}')
