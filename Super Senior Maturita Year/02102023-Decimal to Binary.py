import math
def get_number():
    while True:
        try:
            number = int(input("Enter the number in base 10: "))
            if number > -1: return number
            else: print("The number is lower than 0!")
        except ValueError: print("Invalid input. Please write")
def main():
    number = get_number()
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
if __name__ == "__main__": main()