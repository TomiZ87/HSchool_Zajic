import re
def load(file):
    input_text = open("./Super Senior Maturita Year/files/" + file + ".txt", "r", encoding='utf-8')
    lines = input_text.readlines()
    input_text.close()
    return lines
text = load("28112023-InfoFromText")
times, dates, phones, money, emails, names = ["Time"], ["Date"], ["Phone"], ["Money"], ["Email"], ["Name"]
text[0] = "".join(text)
text[0] = text[0].replace('\n', ' ')
words = text[0].split(" ")
words = [x for x in words if x]
#Checking the parameters
for i, x in enumerate(words):
    if re.match("^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$", x): times.append(x)
    if x.count('.') == 2: dates.append(x) # Datum -> 2 bodky v arrayi
    if re.match("^\d{4}-\d{2}-\d{2}$", x): dates.append(x)
    if re.match("^\d{2}.$", x) and words[i+1] == "apríla": dates.append(x + " " + words[i+1] + " " + words[i+2])
    if ("-" in x) and (len(x) == 13 or len(x) == 11 or len(x) == 12): phones.append(x.strip("."))
    if "£" in x or "€" in x or "$" in x: money.append(x)
    if "EUR" in x or "USD" in x: money.append(words[i-1] + " " + x)
    if "@" in x: emails.append(x)
    if "Ján" in x and (words[i+1] == "Nezmutovaný" or words[i+1] == "Novákom,"): names.append(x.strip(",") + " " + words[i+1].strip(","))
for x in times: print(x, end="; ")
print()
for x in dates: print(x, end="; ")
print()
for x in phones: print(x, end="; ")
print()
for x in money: print(x, end="; ")
print()
for x in emails: print(x, end="; ")
print()
for x in names: print(x, end="; ")