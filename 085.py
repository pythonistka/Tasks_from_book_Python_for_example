name = input("Введите ваше имя: ")
score = 0
name = name.lower()
for i in name:
    if i == "а" or i == "у" or i == "о" or i == "ы" or i == "и" or i == "э" or i == "я" or i == "ю" or i =="ё" or i == "е":
        score = score + 1
print(f"В вашем имени {score} гласных букв")
