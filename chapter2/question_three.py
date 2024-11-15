def findSmallestNumbers(first_number:int, second_number:int, third_number:int):
    first_number = int(input("Enter the first number "))
    second_number = int(input("Enter the second number "))
    third_number = int(input("Enter the third number "))
    sum_result = first_number + second_number + third_number
    product = first_number + second_number * third_number

    if first_number < second_number and first_number < third_number:
        second_number = first_number
    print("the smallest number is ", second_number)
    if first_number > second_number and first_number > third_number:
        first_number = second_number
    print("the largest number is ", first_number)

    print("the sum of the two numbers is ", sum_result)
    print("the product of the two numbers is ", product)
findSmallestNumbers(23,43,56)

