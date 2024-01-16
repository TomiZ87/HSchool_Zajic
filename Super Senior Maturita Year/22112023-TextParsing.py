def load(file):
    input_text = open("./Super Senior Maturita Year/files/" + file + ".txt", "r", encoding='utf-8')
    lines = input_text.readlines()
    input_text.close()
    return lines
def save(saveing_material, file):
    f = open("./Super Senior Maturita Year/files/" + file + ".txt", "w", encoding='utf-8')
    for x in saveing_material: f.write(x)
    f.close()
def get_integer(promt, higher_limit):
    while True:
        try:
            number = int(input(promt))
            if 0 <= number <= higher_limit: return number
            else: ("\033[31mInvalid input. Please enter a valid number. between 0 and " +str(higher_limit)+ "\033[0m")
        except ValueError: print("\033[31mInvalid input. Please enter a valid number.\033[0m")
text = load("22112023-TextParsing")
lines = len(text)
text = "".join(text)
print("Text: " + text)
sentences_num = text.count('?') + text.count('.') + text.count('!')

num_first_sentences = get_integer("How many first sentences do you want to show? >> ", sentences_num)
text = text.replace("!", ".")
text = text.replace("?", ".")
sentences = text.split(".")
sentences.pop(-1) 
sentences = [' '.join(sentence.split()) for sentence in sentences]
for x in range(0, num_first_sentences): 
    if x == 0: print("First " + str(num_first_sentences) + " sentences:")
    print(str(x+1) + ". --> " + sentences[x])
    
num_last_sentences = get_integer("How many last sentences do you want to show? >> ", sentences_num)
sentences.reverse()
for x in range(0, num_last_sentences): 
    if x == 0: print("Last " + str(num_last_sentences) + " sentences:")
    print(str(x+1) + ". --> " + sentences[x])
sentences.reverse()
print("Number of lines: " + str(lines))

words = (text.strip('.').strip(",").strip('?').strip('!')).split(" ")
words = [x.lower() for x in words]
lenghts = []
for x in range(len(words)): lenghts.append(len(words[x]))
longest_word = max(lenghts)
longest_word_index = lenghts.index(longest_word)
print("The longest word is '" + str(words[longest_word_index]) + "' with " + str(longest_word) + " letters.")
letters = 0
for x in text: 
    if x.isalpha(): letters += 1
print("Number of letters: " + str(letters))

max_length_sentence = 0
max_sentence_letters = ''
for x in sentences: 
    letters_in_sentence = sum(y.isalnum() for y in x)
    if letters_in_sentence > max_length_sentence:
        max_length_sentence = letters_in_sentence
        max_sentence_letters = x
print("The longest sentence by letters (" + str(max_length_sentence) + "): "+ str(max_sentence_letters))

max_word_count = 0
max_sentence_by_words = ''
for z in sentences:
    words_of_sentence = z.split()
    word_count = len(words_of_sentence)
    if word_count > max_word_count:
        max_word_count = word_count
        max_sentence_by_words = z
print("The longest sentence by letters (" + str(max_word_count) + "): "+ str(max_sentence_by_words))

word_counts = {} # Dictionary for each word
for individual_word in words: word_counts[individual_word] = word_counts.get(individual_word, 0) + 1
for word, num in word_counts.items():
    if num > 1: print(word + ": " + str(num) + " times")
    
string1 = input("Please enter one sentence: ")
string2 = input("Please enter another sentence: ")
text = load("22112023-TextParsing")
text.insert(0, string1 + "\n")
text.append("\n" + string2)
save(text, "22112023-TextParsing-Output")