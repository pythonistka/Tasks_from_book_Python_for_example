def get_num():
    num = int(input("Введите число: "))
    return num

def count_num(num):
    for i in range(1, num):
        print(i)

def main():
    num = get_num()
    count_num(num)

main()