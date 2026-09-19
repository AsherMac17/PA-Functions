def functionOne():
    print("My student id is ashmac9358")


def functionTwo():
    numberOne = int(input("Please enter a number: "))
    numberTwo = int(input("Please enter a number: "))
    sumValue = numberOne + numberTwo
    print(f"The sum of {numberOne} and {numberTwo} is {sumValue}")
    return sumValue



def functionThree(sumValue):
    if sumValue > 5:
        print("The sum is greater than 5")
    else:
        print("The sum is 5 or less.")
    return 9358



def main():
    functionOne()  # Calls functionOne to show student id
    sumValue = functionTwo()   # Calls functionTwo and stores it returned sum
    studentIdNumber = functionThree(sumValue)   # Passes the sum to functionThree and stores its returned value.
    print(f"functionThree has returned the value of {studentIdNumber}")  # Displays the student ID returned by functionThree
main()
