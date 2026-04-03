class Person:
    def __init__(self, name):
        self._name = name

    def eating(self):
        print(f"{self._name} is eating!")

    def __str__(self):
        return self._name
p = Person("Bob")
print(p)
p.eating()

text = str(p)
print(text)