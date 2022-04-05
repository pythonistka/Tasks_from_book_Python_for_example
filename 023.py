poem = input("Введите строку стихотворения: ")
length_poem = len(poem)
print(f"Длина строки: {length_poem}")

part_of_string_start = int(input("Введите начальную позицию(цифру, начиная с 0): "))
part_of_string_finish = int(input(f"Введите конечную позицию(цифру не более {length_poem} ): "))

result = (poem[part_of_string_start:part_of_string_finish])

print(result)