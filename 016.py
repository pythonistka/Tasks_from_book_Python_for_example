rain = input("Сейчас идет дождь?: ")
rain = rain.lower()
answer = "да"
if rain == answer:
    windy = input("На улице ветренно?: ")
    windy = windy.lower()
    if windy == answer:
        print("Слишком ветренно для зонта")
    else:
            print("Возьмите зонт")
else:
    print("Хорошего дня!")