text = input("Enter the text: ")
diacritics = ["á", "Á", "é", "É", "ě", "Ě", "ä", "Ä", "ó", "Ó", "ú", "Ú", "ý", "Ý", "ĺ", "Ĺ", "ŕ", "Ŕ", "č", "Č", "ď", "Ď", "ľ", "Ľ", "ň", "Ň", "š", "Š", "ť", "Ť", "ž", "Ž", "ô", "Ô", "ł", "Ł"]
diacritics_count = 0
for x in text:
    if x in diacritics:
        print("Diacritics found " + x)
        diacritics_count += 1
if diacritics_count == 0:
    print("No diacritics found!")
else:
    print(str(diacritics_count) + " diacritics found.")
