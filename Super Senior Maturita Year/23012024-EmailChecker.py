email = input("Enter your email: ")
if "@" in email:
    email_content = email.split("@")
    if len(email_content) == 2:
        for x in email_content[0]:
            if x.isdigit() or x.isalpha(): pass
            else:
                print("This is not a valid email! Unknown characters")
                exit()
        if email_content[1].count(".") == 1:
            if 2 <= (len(email_content[1]) - email_content[1].index(".") - 1) <= 4:
                for y in range(0, email_content[1].index(".")):
                    z = email_content[1][y]
                    if z.isdigit() or z.isalpha(): pass
                    else:
                        print("This is not a valid email! Unknown characters --")
                        exit()
                if 3 <= (len(email_content[1]) - (len(email_content[1]) - email_content[1].index("."))) <= 12:
                    print("This is a valid address!")
            else: print("Invalid top level domain!")
        else: print("This is not a valid email! There are either more or none . in the domain name")
    else: print("This is not a valid email! I see more than 1 @")
else: print("This is not a valid email! I see no @")