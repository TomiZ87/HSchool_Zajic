print("Exercise 3: Vowels in word")
letters = []
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
word = str(input("Enter some word: "))
for x in word.lower():
    if x in vowels:
        letters.append(x)
print(letters)