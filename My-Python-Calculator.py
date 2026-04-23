num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operation = input('Enter the operation: ')

match operation:

    case '+':

        res = num1 + num2

    case '-':

        res = num1 - num2

    case '*':

        res = num1 * num2

    case '/':

        res = num1 / num2

print(f'Result: {res}')