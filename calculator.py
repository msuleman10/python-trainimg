#Simple Calculator

firstVal = float(input("Add your first value: "));
lastVal = float(input("Add your last value: "));
operator = input("Add your operator(+ - / *): ");

if operator == '+':
      print(firstVal + lastVal);
elif operator == '-':
      print(firstVal - lastVal);
elif operator == '*':
      print(firstVal * lastVal);
elif operator == '/':
      print(firstVal / lastVal);
else:
      print(f"Provided operator {operator} is not valid please try (+, -, * or /) ");
