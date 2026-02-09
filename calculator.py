

number1 = int(input("Enter first number"))
print(number1)

math = input("Enter an operator:")
print(math)

number2 = int(input("Enter second number"))
print(number2)

if math == "+":
    results = number1 + number2
    print(results)


elif math == "-":
    results = number1-number2
    print(results)

elif math == "*":
    results = number1 * number2
    print(results)

elif math == "/":
    results = number1/number2
    print(results)


