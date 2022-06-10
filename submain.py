def calculate(a, b, formula):
  if formula == '+':
    return a + b
  elif formula == '-':
    return a - b
  elif formula == '*':
    return a * b
  elif formula == '/':
    return a / b
  else:
    return 'You have not typed a valid operator, please run the program again. Closing program...'

print('Enter your first number')
a = float(input())
print('Please enter the operation you would like to perform: * , / , - or +')
formula = input()
print('Enter your second number')
b = float(input())
answer = calculate(a, b, formula)
print(answer)