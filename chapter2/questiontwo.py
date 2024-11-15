def compareNumbers(user_number: int):
    user_number = int(input("Enter any number"))
    square_numbers = user_number * 2
    if square_numbers > 100:
        print("Opps Error trying to check")
    elif square_numbers == 100:
        print("Opps Error trying to check")
    elif square_numbers != 100:
        print("Opps Error trying to check")
    elif square_numbers < 100:
        print("Opps Error trying to check")
    else:
        print("Thank you for your time")

compareNumbers(50)
