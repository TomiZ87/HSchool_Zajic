import math
def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > -1: return number
            else: print("The number is lower than 0!")
        except ValueError: print("Invalid input. Please write")
def DecimalToBinary():
    number = get_number("Enter the number in base 10: ")
    number = float(number)
    final = ""
    while True:
        if number % 2 == 0:
            number = number / 2
            final = '0' + final
        elif number % 2 == 1:
            final = '1' + final
            if number == 1: break
            number = math.floor(number / 2)
    print("Number in binary: " + final)
def BinaryToDecimal():
    binary = get_number("Enter the number in binary: ")
    binary_array = list(str(binary)[::-1])
    binary_array = list(map(int, binary_array))
    final = 0
    for x in range(len(binary_array)):
        final = ((2**x)*binary_array[x]) + final
    print("Number in binary: " + str(final)) 
def main():
    while True:
        choice = input("Enter 1: DecimalToBinary, 2: BinaryToDecimal, 3 to quit the app: ")
        if choice == '1': DecimalToBinary()
        elif choice == '2': BinaryToDecimal()
        elif choice == '3': break
        else: print("\033[31mInvalid choice. Please enter 1, 2, or 3.\033[0m")
if __name__ == "__main__": main()