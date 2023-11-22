sentence = input("Please enter a simple 3-word sentence: ")
words = []
words = sentence.split(" ")
if len(words) == 3:
    if words[-1][-1] == "." or words[-1][-1] == "!":
        words[2] = words[2].replace(".", "?")
        print("Do you " + words[1] + " " + words[2])
    else: print("Do you " + words[1] + " " + words[2] + "?")
else: print("The sentence doesnt have 3 words.")