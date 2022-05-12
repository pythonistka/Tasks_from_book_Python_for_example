import random

def get_nums():
    num_big = int(input("Введите большее число: "))
    num_small = int(input("Введите меньшее число: "))
    comp_num = random.randint(num_small, num_big)
    return comp_num

def guess_num():
    print('Я думаю это номер...')
    num_guess = int(input("Угадай загаданное число: "))
    return num_guess

def compare_num(comp_num, num_guess):
    while num_guess != comp_num:
        if num_guess > comp_num:
            print("Ваше число больше загаданного, попробуйте еще раз.")
        elif num_guess < comp_num:
            print("Ваше число меньше загаданного, попробуйте еще раз.")
        num_guess = int(input("Угадай загаданное число: "))
    if num_guess == comp_num:
        print("Поздравляю, вы угадали!")

def main():
    comp_num = get_nums()
    num_guess = guess_num()
    compare_num(comp_num, num_guess)

main()

