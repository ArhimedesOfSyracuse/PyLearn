def welcome():
    print("Welcome to a very simple calc")
    
def calculate():
    op = input("""
Insert the arithmetic operator of your choice: 
+ for addition 
- for substraction
* for multiplication 
/ for division
** for power
"%" for modulus 
""")

    num1 = float(input("Insert the first number: "))
    num2 = float(input("Insert the second number: "))

    if op == "+":
        print("{} + {} = ".format(num1, num2))
        print(num1 + num2)
    elif op == "-":
        print("{} - {} = ".format(num1, num2))
        print(num1 - num2)
    elif op == "/":
        print("{} / {} = ".format(num1, num2))
        print(num1 / num2)
    elif op == "*":
        print("{} * {} = ".format(num1, num2))
        print(num1 * num2)
    elif op == "**":
        print("{} ** {} = ".format(num1, num2))
        print(num1 ** num2)
    elif op == "%":
        print("{} % {} =".format(num1, num2))
        print(num1 % num2)
    else: 
        print("Wrong opperator hoss!")
    again()
        
def again():
    calc_again = input("""
Do you want to go again? 
Type Y if Yes and N if Not
""")
    if calc_again.upper() == "Y":
        calculate()
    elif calc_again.upper() == "N":
        print("Finished")
    else: 
        again()

welcome()
calculate()
