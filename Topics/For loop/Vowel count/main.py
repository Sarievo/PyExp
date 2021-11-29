string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
count = 0

for char in string:
    for vowel in vowels:
        if char == vowel:
            count += 1
print(count)
