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
  print('\n')
  print('-'*10 + 'MENU' + '-'*10)
  print(''' 1.Addition(+)
  2.Subtraction(-)
  3.Multiplication(*)
  4.Division(/)
  5.Remainder(%)
  ''')
  
  ch = input('Enter the symbol as your choice(+, -, *, /, %): ')

  print('Result:' , claculate(n1, n2, ch))

  exi = input('Wanna Enter More?(y/n)').lower()

  if exi == 'n':
    break

