countries = ("Китай", "Индия", "Япония", "Беларусь", "Армения")
print(type(countries))
print(countries)
country = input("Введите название страны: ")
print(f"По счету ваша страна в списке: {countries.index(country)}")
country_num = int(input("Введите число от 0 до 4: "))
print(f"Страна под номером {country_num}: {countries[country_num]}")