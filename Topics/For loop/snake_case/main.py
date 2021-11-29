string = input()
word_length = len(string)
if not string.islower():
    result = ""
    for i in range(word_length):
        if i == 0 and not string[i].islower():
            result += string[i].lower()
        else:
            result += "_" + string[i].lower() if string[i].isupper() else string[i]
    print(result)
else:
    print(string)
