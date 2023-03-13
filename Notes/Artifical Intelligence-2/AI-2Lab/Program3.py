import string
paragraph = input("Enter a paragraph: ")
paragraph = paragraph.translate(str.maketrans("", "", string.punctuation))
num_spaces = paragraph.count(" ")
print("")
print(f"Paragraph without punctuation: {paragraph}")
print("")
print(f"Number of spaces: {num_spaces}")