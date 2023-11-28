import re, datetime
def load(file):
    input_text = open("./Super Senior Maturita Year/files/" + file + ".txt", "r", encoding='utf-8')
    lines = input_text.readlines()
    input_text.close()
    return lines
text = load("28112023-InfoFromText")
text[0] = "".join(text)
text[0] = text[0].replace('\n', ' ')
words = text[0].split(" ")
words = [x for x in words if x]
#Checking the parameters
for i, x in enumerate(words):
    if re.match("^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$", x): print("Time: " + x)
    if ("-" in x) and (len(x) == 13 or len(x) == 11 or len(x) == 12): print("Phone number: " + x.strip("."))
    if "@" in x: print("Email address: " + x)
    if x.count('.') == 2: print("Date: " + x) # Datum -> 2 bodky v arrayi
    if re.match("^\d{4}-\d{2}-\d{2}$", x): print("Date: " + x)
    if "£" in x or "€" in x or "$" in x: print("Currency: " + x)
    if "EUR" in x or "USD" in x: print("Currency: " + words[i-1] + " " + x)
    if "Ján" in x or "Nezmutovaný" in x or "Novák" in x: print("Name " + x)
    if re.match("^\d{2}.$", x): print("Date: " + x + " " + words[i+1] + " " + words[i+2])