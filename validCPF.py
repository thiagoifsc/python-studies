#!/usr/bin/python
import sys

# function to remove all non numeric chars and check if the list has 11 elements or has all equal digits(invalid CPFs)
def checkDigits(cpfInput):
    cpfOnlynumbers = [int(digit) for digit in cpfInput if digit.isdigit()]
    equal = all(element == cpfOnlynumbers[0] for element in cpfOnlynumbers)
    if not cpfOnlynumbers.__len__() == 11 or equal:
        print(False)
        exit(0)
    
    return(cpfOnlynumbers)

# function to calculate the verifing digits of the CPF
def checkCPFlogic(cpfOnlyNumbers):
    # removes last 2 digits
    cpfWithCalcDigit = cpfOnlyNumbers[:]
    del cpfWithCalcDigit[-2]

    # calculates the first verifing digit
    firstCpfMultiplier = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    firstDigit = sum([a * b for a, b in zip(cpfOnlyNumbers, firstCpfMultiplier)])%11
    if (firstDigit < 2):
        firstDigit = 0
    else:
        firstDigit = 11-firstDigit

    # calculates the second verifing digit
    secondCpfMultiplier = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    cpfWithCalcDigit.insert(9, firstDigit)
    secondDigit = sum([a * b for a, b in zip(cpfWithCalcDigit, secondCpfMultiplier)])%11
    if (secondDigit < 2):
        secondDigit = 0
    else:
        secondDigit = 11-secondDigit

    # checks with calculated digits match user input and returns the result
    if cpfOnlyNumbers[9] == firstDigit and cpfOnlyNumbers[10] == secondDigit:
        valid=True
    else:
        valid=False
    return(valid)
    
# main loop
if sys.argv[1:]:
    cpfInput = str(sys.argv[1])
else:
    cpfInput = input("Enter the CPF for validation: ")
cpfOnlyNumbers = checkDigits(cpfInput)
isValidCPF = checkCPFlogic(cpfOnlyNumbers)
print(isValidCPF)