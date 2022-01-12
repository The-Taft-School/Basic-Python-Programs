
num_a = float(input('gimme a side: '))
num_b = float(input('gimme another side: '))
num_c = float(input('and another one: '))

s = (num_a + num_b + num_c) / 2

area = (s * (s - num_a) * (s - num_b) * (s - num_c)) ** 0.5

print(f"ur triangle looks cool it's {area} big")
