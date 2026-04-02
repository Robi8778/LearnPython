raining = False
temperature = 18

if temperature > 19 and not raining:
    print("Weather fine")
elif not raining:
    print("its dry")
else:
    print("stay indoors")

mood = "good" if not raining else "bad"
print(mood)