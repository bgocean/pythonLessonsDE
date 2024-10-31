class Human:
    _name: str
    _location: str

    def __init__(self, name='Ivan'):
        self._name = name
        self._location = 'Kiev'

    def get_name(self):
        return self._name

    def get_location(self):
        return self._name + ': ' + self._location

    def set_location(self, location):
        self._location = location


class Children(Human):
    _age = 5

    def __init__(self, name='Vasya'):
        super().__init__(name)

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._name + ': ' + str(self._age)

class Bus:
    __children: list()

    def __init__(self, children: list):
        self.__children = children

    def add_children(self, children: list):
        self.__children += children

    def remove_children(self, children: list):
        for one_child in children:
            if one_child in self.__children:
                self.__children.remove(one_child)


first_child = Children()
second_child = Children('Petya')
third_child = Children('Igoryok')
one_child = Children()
print(one_child.get_location())
print(one_child.get_age())
