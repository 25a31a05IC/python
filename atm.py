m = 8000
pin = 123

ep = int(input("Enter pin: "))

if ep != pin:
    print("incorrect pin")
else:
    print("Balance enquiry-1")
    print("Cash withdraw-2")
    print("Fast cash-3")

    ch = int(input("Choose your option: "))

    if ch == 1:
        print("Your balance amount is:", m)

    elif ch == 2:
        a = int(input("Enter amount in digits: "))
        if a > m:
            print("insufficient balance")
        elif a % 100 != 0:
            print("enter two zero digit")
        else:
            print("Your amount has been credited")
            m = m - a
            print("your balance amount is:", m)

    elif ch == 3:
        print("5000-1")
        print("10000-2")
        print("15000-3")
        print("20000-4")

        op = int(input("Choose your amount: "))

        if op == 1:
            if 5000 > m:
                print("insufficient balance")
            else:
                m -= 5000
                print("Your balance amount is:", m)

        elif op == 2:
            if 10000 > m:
                print("insufficient balance")
            else:
                m -= 10000
                print("Your balance amount is:", m)

        elif op == 3:
            if 15000 > m:
                print("insufficient balance")
            else:
                m -= 15000
                print("Your balance amount is:", m)

        elif op == 4:
            if 20000 > m:
                print("insufficient balance")
            else:
                m -= 20000
                print("Your balance amount is:", m)

        else:
            print("enter valid number")

    else:
        print("Enter valid option")
