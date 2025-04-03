print("Hi")
print("lokesh")
print("CBIT")
print("CSE")
def calculator():
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    if op == "+":
        print('addition operation')
        print(num1+num2)
        print('Result(num1+mun2)')
    elif op == "-":
       print('addition operation')
       print(num1+num2)
       print('Result(num1+mun2)')
    elif op == "*":
         print('addition operation')
         print(num1+num2)
         print('Result(num1+mun2)')
    elif op == "/":
        return "Error! Division by zero." if num2 == 0 else num1 / num2
    else:
        return "Invalid operator!"
print(calculator())