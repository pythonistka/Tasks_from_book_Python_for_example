two_dim_dict = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694}, "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612}, "Anna": {"N": 5239, "S": 4802, "E": 5820, "W": 1859}, "Flona": {"N": 3904, "S": 3645, "E": 8820, "W": 2451}}
name = input("Введите имя продавца (John, Tom, Anna, Flona): ")
name = name.title()
region = input("Введите регион (N, S, E, W): ")
region = region.upper()
print(f"Объем продаж у {name} в регионе {region}: {two_dim_dict [name] [region]}")

change_name = input("Введите имя продавца, у которого хотите заменить объем продаж (John, Tom, Anna, Flona): ")
change_name = change_name.title()
change_region = input("Введите регион, у которого хотите заменить объем продаж (N, S, E, W): ")
change_region = change_region.upper()
change_sales = int(input("Введите новый объем продаж: "))

two_dim_dict [change_name] [change_region] = change_sales

print(f"Объемы продаж у {change_name} по всем регионам: {two_dim_dict [change_name]}")
