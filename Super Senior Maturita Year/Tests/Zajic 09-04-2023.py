file = open("./Super Senior Maturita Year/files/09042024-Task.txt", "r", encoding="utf-8")
textik = file.read()
file.close()

results = []
sentences = [0, 0, 0]

for x in range(len(textik)):
    if textik[x] == '.': sentences[0] += 1
    elif textik[x] == '!': sentences[1] += 1
    elif textik[x] == '?': sentences[2] += 1

textik = textik.replace(".", "!")
results.append(textik + "\n")
results.append("Pocet vsetkych viet " + str(sentences[0]+sentences[1]+sentences[2]) + "\n")
results.append("Opytovacie (Otazniky) " + str(sentences[2]) + "\n")
results.append("Rozkazovacie (Vykricniky) " + str(sentences[1]) + "\n")
results.append("Oznamovacie (Bodky) " + str(sentences[0]) + "\n")
file2 = open("./Super Senior Maturita Year/files/09042024-Result.txt", "w", encoding="utf-8")
for x in results:
    file2.write(x)
file2.close()
