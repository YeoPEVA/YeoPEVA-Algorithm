vowels = {'a', 'e', 'i', 'o', 'u'}

while True:
    word = input()
    if word == "#":
        break

    if word[0] in vowels:
        result = word + "ay"
    else:
        for i, ch in enumerate(word):
            if ch in vowels:
                result = word[i:] + word[:i] + "ay"
                break
        else:
            result = word + "ay"

    print(result)