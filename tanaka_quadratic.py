import math

a = float(input('Give me a number: '))
b = float(input('This is like madlibs give me another number: '))
c = float(input('Anotha one: '))
d = int(input('Mooooreeeee but make this one an integer: '))
e = float(input('Okay last one: '))
f = float(input("You're so gullible but this is actually the last one: "))

solution = math.ceil(a) * b ** c - math.factorial(d) / e + math.floor(f)

print(f"You got {solution}. ok cool bye.")
