print("Exercise 1: Division of Numbers")
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
if(first_num % second_num == 0):
    result = first_num/second_num
    print("The number is divisible by " + str(second_num) + ". Equation: " + str(first_num) + "/" + str(second_num) + "=" + str(result))
else:
    result = first_num/second_num
    print("The number is not divisible by " + str(second_num) + ". Equation: " + str(first_num) + "/" + str(second_num) + "=" + str(result) + " Remainder: " + str(first_num % second_num))

print("Exercise 2: Odd/Even Numbers")
first_num = int(input("Enter the first number: "))
if(first_num % 2 == 0):
    print("The number is even.")
else:
    print("The number is odd.")

print("Exercise 3: And and Or")
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
if(first_num % 2 == 0 and second_num % 2 == 0) or (first_num % 2 != 0 and second_num % 2 != 0):
    print("Yes")
else:
    print("No")

print("Exercise 4: The character e")
string_E = input("Write here some word: ")
if "e" in string_E:
    print("There is the character e in word " + string_E)
else:
    print("There isn't the character e in " + string_E)

print("Exercise 5: Vowels")
string_vowel = input("Write here some word: ")
if "a" in string_vowel or "e" in string_vowel or "i" in string_vowel or "o" in string_vowel or "u" in string_vowel or "y" in string_vowel:
    print("There is at least one vowel in word " + string_vowel)
else:
    print("There isn't any vowel in word " + string_vowel)

print("Exercise 6: Comparison of Numbers")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a<c<b:
    print("a<c<b occured: " + str(a) +"<" + str(c) + "<" + str(b))
else:
    if b<c<a:
        print("a<c<b occured: " + str(b) +"<" + str(c) + "<" + str(a))
    else:
        print("a<c<b nor b<c<a didn't occured")

