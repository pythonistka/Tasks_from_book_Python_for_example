import random

fortune = random.choice(["о", "р"])
answer = input("Орёл или решка? (о/р): ")
if answer == fortune:
    print("Вы победили!")
else:
    print("Плохая попытка")

print(f"Мы загадали {fortune}")