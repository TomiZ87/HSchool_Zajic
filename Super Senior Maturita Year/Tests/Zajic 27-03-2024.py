def load():
    input_text = open("./Super Senior Maturita Year/files/27032024-Task.txt", "r", encoding='utf-8')
    text = input_text.read()
    input_text.close()
    return text
def save(mats):
    f = open("./Super Senior Maturita Year/files/27032024-Result.txt", "w", encoding='utf-8')
    for x in mats: f.write(x)
    f.close()
result = []
textik = load()
print(textik)
result.append(textik + "\n\n")
textik1 = textik.split(" ")
email = []
tld = []
for x in textik1:
    if "@" in x:
        if x[-1] == ".":
            x = x[:-1]
            textik = textik.replace(x, x.upper())
            if x[-3] == "." and x[-2:] not in tld:
                tld.append(x[-2:])
            elif x[-4] == "." and x[-3:] not in tld:
                tld.append(x[-3:])
            print(tld)
            print(x)
        email.append(x.upper())
result.append(textik + "\n\n")
print(textik)

tld.sort()
result.append("Počet emilov:  " + str(len(email)) + "\n")
result.append("Počet unikátnych top level domains:  " + str(len(tld)) + "\n")
result.append("Zoznam top level domain v abecednom poradí:  " + ", ".join(tld) + "\n")

save(result)