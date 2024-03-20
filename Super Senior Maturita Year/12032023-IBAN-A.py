def load(file):
    input_text = open("./Super Senior Maturita Year/files/" + file + ".txt", "r", encoding='utf-8')
    lines = input_text.readlines()
    input_text.close()
    lines = [line.rstrip('\n') for line in lines]
    return lines
def save(saveing_material, file):
    f = open("./Super Senior Maturita Year/files/" + file + ".txt", "w", encoding='utf-8')
    for x in saveing_material: f.write(x)
    f.close()
output = []
ibans = load("IBAN-codes")
for x in range(len(ibans)):
    ibans[x] = ibans[x].replace(" ", "")
output.append("There are " + str(len(ibans)) + " ibans.\n")
iban_banks = load("IBAN-banks")
for x in range(len(iban_banks)):
    iban_banks[x] = iban_banks[x].split(" - ")
iso_codes = load("iso_2digit_alpha_country_codes_IBAN")
for x in range(len(iso_codes)):
    iso_codes[x] = iso_codes[x].split("\t")
dic_country = {}
dic_bank = {}
valids = 0
for _iban in ibans:
    temp = _iban
    if not _iban.isalnum() or len(_iban) < 15 or len(_iban) > 31:
        pass
    else:
        _iban = (_iban[4:] + _iban[0:4]).upper()
        _iban = ''.join(str(10 + ord(char) - ord('A')) if char.isalpha() else char for char in _iban)
        if int(_iban) % 97 == 1: 
            valids += 1
            for y in iso_codes:
                if temp[:2] in y[0]:
                    if temp[:2] in dic_country:
                        dic_country[temp[:2]] += 1
                    else: 
                        dic_country[temp[:2]] = 1
            if temp[:2] == "SK":
                for z in iban_banks:
                    if temp[4:8] in z[0]:
                        if temp[4:8] in dic_bank:
                            dic_bank[temp[4:8]] += 1
                        else: 
                            dic_bank[temp[4:8]] = 1
output.append("There were " + str(valids) + " valid ibans.\n")
for country in dic_country:
    for y in iso_codes:
        if country in y[0]:
            country_name = y[1]
    output.append(country_name + " " + str(dic_country[country]) + "\n")
for bank in dic_bank:
    for y in iban_banks:
        if bank in y[0]:
            bank_name = y[1]
    output.append(bank_name + " " + str(dic_bank[bank]) + "\n")


save(output, "IBAN_A")
