nums = []
for i in range(3):
        num = int(input('Введите число: '))
        nums.append(num)
        print(nums)
answer = input("Хотите ли вы оставить последнее введенное число в списке?(да/нет): ")
if answer == "нет":
    nums.pop()
print(nums)