def calculate(w, h, l):
    return w*h*l

area = calculate(5,l=5,h=5)
print(area)

def catalogue(name, *args):
    print("Type: ", type(args))
    print(name)

    if len(args) >= 1:
        print(args[0])

    for value in args:
        print(value)

catalogue("Trees", "oak", "ash")
print()

def details(name, **kwargs):
    print(type(kwargs))
    print(kwargs)

    if "height" in kwargs:
        print(kwargs["height"])

    for key in kwargs:
        print(key, kwargs[key])

details("Sue", height = 170, age = 42)