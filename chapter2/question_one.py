def findSquaresOfEachNumbers(first_number: int, second_number: int):
    for index in first_number, second_number:
        first_number = int(input("Enter first number "))
        second_number = int(input("Enter second number "))
        #print the squares of the two numnbers
        result = first_number * 2
        second_result = second_number * 2
        print(result)
        print(second_result)
        #print the sum of the squares
        sum_result = result + second_result
        print(sum_result)

        #print the difference of the squares
        difference_result = result - second_result
        print(difference_result)

findSquaresOfEachNumbers(10, 30)
