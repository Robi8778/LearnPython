fruits = ["a", "o", "g"]
print(id(fruits))

fruits += ["m"]
print(id(fruits))
print(fruits)

fruits[0] = "s"
print(fruits)

fruits.append("p")
fruits.extend(['a', 'b'])

fruits.insert(2, "kiwi")
print(fruits)

fruits_tuple = tuple(fruits)
print(fruits_tuple)

fruits_list = list(fruits_tuple)
print(fruits_list)