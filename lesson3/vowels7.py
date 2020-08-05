vowels = {"a",'e','i','o','u'}
word = input("введите слово для поиска гласных:")
i = list(vowels.intersection(set(word)))
for vowel in i:
    print(vowel)