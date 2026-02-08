# Make four functions, add, subtract, multiply, and divide. Based on what the user wants to do, that specific funciton will be used. The user must also provide 2 numbers for calculations.

action = int(input("Please choose one operation, 1 for additon, 2 for subtraction, 3 for multiplication or 4 for division: "))
number1 = int(input("Please provide one number: "))
number2 = int(input("Please provide a second number: "))

def add(number1,number2):
  
  sum = number1 + number2
  print(f"{number1} + {number2} = {sum}")

def subtract(number1,number2):
 sum = number1 - number2
 print(f"{number1} - {number2} = {sum}")

def multiply(number1,number2):
  sum = number1 * number2
  print(f"{number1} * {number2} = {sum}")

def divide(number1,number2):
  sum = number1/number2
  print(f"{number1} / {number2} = {sum}")


if action==1:
  add(number1,number2)


elif action==2:
  subtract(number1,number2)

elif action==3:
  multiply(number1,number2)

elif action==4:
  divide(number1,number1)

else:
  print("Please give a valid option")