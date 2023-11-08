word = input("Enter your word to check for palindromes: ")
word = word.lower()

if word == word[::-1]: print("1/2 The word '"+ str(word) + "' IS palindrome.")
else: print("1/2 The word '"+ str(word) + "' IS NOT palindrome.")

reversed_word = ""
for char in word:
    reversed_word = char + reversed_word
if word == reversed_word: print("2/2 The word '"+ str(word) + "' IS palindrome.")
else: print("2/2 The word '"+ str(word) + "' IS NOT palindrome.")
