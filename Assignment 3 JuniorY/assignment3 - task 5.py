print("Exercise 5: Mini dictionary")
entered_word = input("Enter one of these words (apple, dog, cat, horse): ")
dictionary = {
  "english": "slovak",
  "apple": "jablko",
  "cat": "mačka",
  "dog": "pes",
  "horse": "kôň"
}
if entered_word in dictionary:
    print("The english translation is " + str(dictionary[entered_word])) 
else:
    print("Invalid word")