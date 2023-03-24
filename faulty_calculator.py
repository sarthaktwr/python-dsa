import math
import string

input_number1 = int(input("Enter a number: "))
input_number2 = int(input("Enter another number: "))
input_op = str(input("Enter operation you want: "))
input_op == string.capwords(input_op)

if input_op == 'Divide' or input_op == 'Multiplication' or input_op == 'Addition' or input_op == 'Subtraction':
    if input_op == 'Divide':
        if input_number1 == 56 and input_number2 == 6:
            print('4')
        else:
            print(f'{int(input_number1 / input_number2)}')
    elif input_op == 'Multiplication':
        if input_number1 == 45 and input_number2 == 3:
            print('555')
        else:
            print(f'{int(input_number1 * input_number2)}')
    elif input_op == 'Addition':
        if input_number1 == 56 and input_number2 == 9:
            print('77')
        else:
            print(f'{int(input_number1 + input_number2)}')
    elif input_op == 'Subtraction':
        print(f'{int(input_number1 - input_number2)}')
else:
    print("enter correct operation")