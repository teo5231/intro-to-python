name = 'tampakis'
fatsa = ':)'
print(f"Welcome {name}.{fatsa}")

namelist = ['teo', 'tampakis', 'nao', 'john']
agelist = [52, 15, 15, 15]
print(f"Welcome {namelist[0]} {fatsa}. you are {agelist[0]} years old ")
print(f"Welcome {namelist[1]} {fatsa}. you are {agelist[1]} years old ")
print(f"Welcome {namelist[2]} {fatsa}. you are {agelist[2]} years old ")
print(f"Welcome {namelist[3]} {fatsa}. you are {agelist[3]} years old ")

agelist[0] = 45
print(f"Welcome {namelist[0]} {fatsa}. you are {agelist[0]} years old ")
print(agelist)
print(namelist)

for name in namelist:
    print(f"Welcome {name}")
for age in agelist:
    print(f"your age is {age}")

for i in [0, 1, 2, 3]:
    print(f"Welcome {namelist[i]} you are {agelist[i]}")