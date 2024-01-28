# Here we are going to make a calculator in python 
from art import logo
def calculator():
    print(logo)
    n1 = float(input("Enter your first number: "))
    def add(n1, n2):
        return n1+n2
    def subtract(n1, n2):
        return n1-n2
    def multiply(n1, n2):
        return n1*n2
    def divide(n1, n2):
        return n1/n2

    operations = {"+": add,
                "-": subtract,
                "*": multiply,
                "/": divide
    }
    for symbol in operations:
        print(symbol)
    opeartions_symbols = input(" Pick an opeartion from the line above: ")
    n2 = float(input("Enter your second number: "))
    new_operations = operations[opeartions_symbols] 
    first_answer = new_operations(n1, n2)

    print(f"{n1} {opeartions_symbols} {n2} = {first_answer}")
    further_calculation = True
    while further_calculation:
        further_calculation =  input(f"Do you wanna do further calculation with {first_answer}? type 'yes' or 'no':  ")
        if further_calculation == "yes":
            new_operations_symbols = input("Pick an opeartions front he line above: ")
            n3 = float(input("What is the next number: "))
            new_operations = operations[new_operations_symbols]
            second_answer = new_operations(first_answer, n3)
            print(f"{first_answer} {new_operations_symbols} {n3} = {second_answer}")
        else:
            further_calculation = False
            calculator()
calculator()






