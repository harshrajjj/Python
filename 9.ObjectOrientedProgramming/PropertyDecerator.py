class tealeaf:
    def __init__(self,age):
        self._age = age

    @property
    def age(self):
        return self._age+ 2
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


leaf = tealeaf(5)
print(leaf.age)  # Output: 7
leaf.age = 10
print(leaf.age)  # Output: 12
try:
    leaf.age = -3
except ValueError as e:
    print(e)  # Output: Age cannot be negative