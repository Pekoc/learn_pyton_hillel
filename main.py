###### Homework #########
print("Welcome to calculator")
try:
    value_float_1 = float(input("Please type a number: "))
    value_float_2 = float(input("Please type another number: "))
    value_operator = input("Please choose operator:\n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/'\n your answer:")

    if value_operator in "1,2,3,4,":
        print("Incorrect choose of operation")
    else:

        if value_operator == '1':
            result = value_float_1 + value_float_2

        elif value_operator == '2':
            result = value_float_1 - value_float_2

        elif value_operator == '3':
            result = value_float_1 * value_float_2

        elif value_operator == '4':
            result = value_float_1 / value_float_2

        else:
            print("Incorrect choose of operation")
except ValueError:
        print("Enter the number")

except ZeroDivisionError:
        print("Invalid operation")