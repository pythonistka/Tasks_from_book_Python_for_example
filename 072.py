lessons = ["Физкультура", "ОБЖ", "Математика", "Физика", "Биология", "Литература"]
print(lessons)
lessons_bad = input("Введите предмет, который вам не нравится: ")
lessons.remove(lessons_bad)
print(lessons)