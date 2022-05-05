print("1). Создать новый файл")
print("2). Показать файл")
print("3). Добавить новый элемент в файл")

answer = int(input("Выберите один из вариантов (1, 2, 3): "))

if answer == 1:
    file = open("Subject.txt", "w")
    subject = input("Введите название школьного предмета: ")
    file.write(subject + "\n")
    file.close()

elif answer == 2:
    file = open("Subject.txt", "r")
    print(file.read())
    file.close()

elif answer == 3:
    file = open("Subject.txt", "a")
    subject = input("Введите название школьного предмета: ")
    file.write(subject + "\n")
    file.close()

    file = open("Subject.txt", "r")
    print(file.read())
    file.close()

else:
    print("Вы выбрали отсутствующий вариант ответа")