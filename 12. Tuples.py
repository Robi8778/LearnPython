#Containers

stuff = ("Charles", 6, 5.3, False)

print(stuff[0])

# stuff[1] = 2 -> Type Error
a, b, c, d = stuff

person, number1, *other = stuff

print(other)

animlas = "cat", "dog"

animal = ("cat",)
print(animal)