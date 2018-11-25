
card_number ='18720156188'
card_password='060429'
enter1 = raw_input("Please enter your card number: ")
enter2 = raw_input("Please enter your card password: ")
if enter1==card_number:
    if enter2==card_password:
        print("You have one billion!")
    else:
        print("The number or the password is wrong.")
elif enter2==card_password:
    enter1=raw_input("The number is wrong.Please enter again:")
    if enter1==card_number:
        print("You have one billion!")
    else:
        print("The number or the password is wrong.")
elif enter1==card_number:
    enter2=raw_input("The password is wrong.Please enter again:")
    if enter2==card_password:
        print('You have one billion!')
    else:
        print("The number or the password is wrong.")
else:
    print("The number and the password are wrong.")

