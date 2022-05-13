import random

def add():
    num_add_1 = random.randint(5, 20)
    num_add_2 = random.randint(5, 20)
    print(f"Сколько будет {num_add_1} + {num_add_2}?")
    answer_correct = num_add_1 + num_add_2
    answer_add = int(input("Введите ваш ответ: "))
    answers = (answer_correct, answer_add)
    return answers

def subtraction():
    num_add_3 = random.randint(25, 50)
    num_add_4 = random.randint(1, 25)
    print(f"Сколько будет {num_add_3} - {num_add_4}?")
    answer_correct = num_add_3 - num_add_4
    answer_add = int(input("Введите ваш ответ: "))
    answers = (answer_correct, answer_add)
    return answers

def chek(answer_correct, answer_add):
    if answer_correct == answer_add:
        print("Ответ верный")
    else:
        print(f"Ваш ответ неверный, правильный ответ: {answer_correct}")

def main():
    print("1) Сложение")
    print("2) Вычитание")
    select = int(input("Выберите 1 или 2: "))
    if select == 1:
        answer_correct, answer_add = add()
        chek(answer_correct, answer_add)
    elif select == 2:
        answer_correct, answer_add = subtraction()
        chek(answer_correct, answer_add)
    else:
        print("Некорректный выбор")

main()