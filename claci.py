print('Welcome to Python Calculator App')

def claculate(a, b, c):
  if c == '+':
    return a + b
  elif c == '-':
    return a - b
  elif c == '*':
    return a*b
  elif c == '/':
    return a/b
  elif c == '%':
    return a%b

while True:
  
  n1 = int(input('Enter the 1st Number: '))
  n2 = int(input('Enter the 2nd Number:'))

  print('-'*10 + 'MENU' + '-'*10)