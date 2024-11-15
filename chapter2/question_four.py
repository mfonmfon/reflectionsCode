def largestAndSmallestNumbers(numberOne: int, numberTwo: int, numberThree: int, numberFour: int, numberFive: int):
    numberOne = int(input("Enter the first number"))
    numberTwo = int(input("Enter the second number"))
    numberThree = int(input("Enter the third number"))
    numberFour = int(input("Enter the fourth number"))
    numberFive = int(input("Enter the fifth number"))

    largestNumber: int = 0
    smallest_number: int = 0

    if numberOne > numberTwo and numberOne > numberTwo and numberOne > numberThree and numberOne > numberFour and numberOne > numberFive:
        largestNumber = numberOne
    if numberOne < numberTwo < numberThree and numberTwo > numberFour and numberTwo > numberFive:
        smallest_number = numberTwo

    print("the largest number is ", largestNumber)
    print("the smallest number is ", smallest_number)
largestAndSmallestNumbers(12, 43,5,43,21)