filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    content = file.read()
    words = content.split()
    num_words = len(words)
    print(f'The file "{filename}" contains {num_words} words.')
