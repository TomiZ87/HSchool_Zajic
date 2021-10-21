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

