bottles = 10
while bottles > 0:
    print(f"На стене висит {bottles} зелёных бутылок. 1 зелёная бутылка падает на пол.")
    bottles = bottles - 1
    num = int(input("Сколько зеленых бутылок осталось висеть на стене?: "))
    if num == (bottles):
        print(f"Верно, осталось {bottles} бутылок на стене")
    else:
        num = int(input("Попробуй еще раз. Сколько зеленых бутылок осталось висеть на стене?: "))
print("На стене не осталось ни одной бутылки" )

