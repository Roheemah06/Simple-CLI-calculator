# Simple CLI calculator using python
print("simple CLI calculator")

is_running = True

while is_running:
  print("Loading")
  user_operation = input ( "Which operation would you like to perform?\nSelect any of ['+','-','*','/','%'] : ")

  #accept input
  num1 = float(input("Enter first number:"))
  num2 = float(input("Enter second number: "))

  if user_operation == "+":
    print(num1 + num2)
  elif user_operation == "-":
    print(num1 - num2)
  elif user_operation == "*":
    print(num1 * num2)
  elif user_operation == "/":
    print(num1 / num2)
  elif user_operation == "%":
    print(num1 % num2)
  else:
    print("math error")

  choice = input("Will you like to perform another calculation. [T,F] :")
  if choice == "T":
    pass

  if choice == "F":
    is_running = False

