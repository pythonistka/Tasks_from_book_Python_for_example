import csv

file = open("Books.csv", "w")
new_info = "To Kill a Mockingbird, Harper Lee, 1960\n"
file.write(str(new_info))
new_info = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(new_info))
new_info = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(str(new_info))
new_info = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(str(new_info))
new_info = "Pride and Prejudice, Jan Austen, 1813\n"
file.write(str(new_info))
file.close()