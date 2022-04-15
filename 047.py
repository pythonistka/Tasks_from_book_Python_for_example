num = int(input("Введите первое число для сложения: "))
num_second = int(input("Введите второе число для сложения: "))
result = num + num_second
question = input("Желаете прибавить еще число?(да/нет): ")
answer = "да"
while question == answer:
    num_third = int(input("Введите число для сложения: "))
    result = result + num_third
    question = input("Желаете прибавить еще число?(да/нет): ")
print(f"Сумма всех чисел равна: {result}")
