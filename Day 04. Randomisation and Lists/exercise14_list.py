#banker roulette

from random import randint
names = []
qtd = int(input("How many people are there? (type 'done' to finish earlier)\n"))
for i in range(1, qtd + 1):
    name_person = input(f"Type the {i} name\n").title()
    names.append(name_person)
    if name_person == 'done':
        break

len_names = len(names)
random = randint(0, len_names -1)
name_payer = names[random]

print(f"{name_payer} will pay all the bill!")