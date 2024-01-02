def add(x, y):
 return x + y

def subtract(x, y):
 return x - y

def multiply(x, y):
 return x * y

def divide(x, y):
 if y == 0:
     return "Cannot divide by zero."
 else:
     return x / y

def power(x, y):
 return x ** y

def modulo(x, y):
 if y == 0:
     return "Cannot modulo by zero."
 else:
     return x % y

print("Welcome to the Calculator")

while True:
 print("\nSelect operation.")
 print("1.Add")
 print("2.Subtract")
 print("3.Multiply")
 print("4.Divide")
 print("5.Power")
 print("6.Modulo")
 print("7.Exit")

 choice = input("Enter choice(1-7): ")

 if choice in ('1', '2', '3', '4', '5', '6', '7'):
     if choice != '7':
         num1 = float(input("Enter first number: "))
         num2 = float(input("Enter second number: "))

         if choice == '1':
             print(num1, "+", num2, "=", add(num1, num2))

         elif choice == '2':
             print(num1, "-", num2, "=", subtract(num1, num2))

         elif choice == '3':
             print(num1, "*", num2, "=", multiply(num1, num2))

         elif choice == '4':
             print(num1, "/", num2, "=", divide(num1, num2))

         elif choice == '5':
             print(num1, "^", num2, "=", power(num1, num2))

         elif choice == '6':
             print(num1, "%", num2, "=", modulo(num1, num2))
     else:
         print("Thank you for using the Calculator. Goodbye!")
         break
 else:
     print("Invalid Input")
