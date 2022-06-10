# Simple CLI Calculator
print("Welcome to Simple CLI Calculator")

isRunning = True 

while isRunning:
    # Processing Calculations...
    print("Starting Calculator Process")
    userOperation = input("What operation would you like to perform?\nPick any of ['+','-','*', '/', '%'] : ")

    # Get user numbers
    try: # Try to get user numbers, if they're valid integers/floats, continue
        number1 = float(input("First number: "))
        number2 = float(input("Second number: "))
    
    except: # We get an error when running it
        print("Failed, invalid numbers...")
        continue 

    if userOperation == "+":
        # perform addition
        print(number1 + number2)

    elif userOperation == "-":
        # perform subtraction
        print(number1 - number2)

    elif userOperation == "*":
        # perform multiplication
        print(number1 * number2)

    elif userOperation == "/":
        # perform division
        print(number1 / number2)

    elif userOperation == "%":
        # perform division
        print(number1 % number2)

    else:
        # Invalid operation
        print("Invalid operation entered, try again...")
    
    choice = input("Would you like to run another calculation. [y,n] :")
    if choice == "y":
        pass 
    
    if choice == "n":
        isRunning = False 
        # same thing as a break.

print("Thanks for using Simple Calculator, bye bye...see you another time")
