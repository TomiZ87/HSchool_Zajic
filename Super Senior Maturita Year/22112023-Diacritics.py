import string
text = input("Enter the text: ")
diacritics = string.ascii_letters
diacritics_count = 0
for x in text:
    if x not in diacritics:
        print("Diacritics found " + x)
        diacritics_count += 1
if diacritics_count == 0: print("No diacritics found!")
else: print(str(diacritics_count) + " diacritics found.")
