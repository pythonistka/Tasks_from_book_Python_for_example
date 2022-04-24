verse = "Я помню чудное мгновенье: Передо мной явилась ты, Как мимолетное виденье, Как гений чистой красоты."
print(verse)
amount = len(verse)
end_num = amount - 1
start = int(input(f"Введите начальную позицию от 0 до {end_num}: "))
start_for_finish = start + 1
finish = int(input(f"Введите начальную позицию от {start_for_finish} до {end_num}: "))
print(verse[start:finish])