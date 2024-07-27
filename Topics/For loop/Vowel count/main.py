string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

count_vowels = 1

for letter in string:
    if letter in vowels:
        count_vowels += 1

print(count_vowels)