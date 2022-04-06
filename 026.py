word = input("Введите слово: ")
letter_first = (word[0])
length_word = len(word)
base = word[1:len(word)]
suffix = "ау"

if letter_first == "а" or letter_first == "и" or letter_first == "о" or letter_first == "у" or letter_first == "ы" or letter_first == "э" or letter_first == "е" or letter_first == "ё" or letter_first == "ю" or letter_first == "я":
    new_word = word + suffix
    new_word = new_word.lower()
else:
    new_word = base + letter_first + suffix
    new_word = new_word.lower()

print(new_word)