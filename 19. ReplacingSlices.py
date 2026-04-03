numbers = list((0,1,2,3,4,5))
numbers[2:4] = (0,0,0,0)
print(numbers)

numbers[2:5] = []
print(numbers)

#extended slice syntax

print(numbers[1::2])
numbers[1::2]= ['A', 'b']

print(numbers)