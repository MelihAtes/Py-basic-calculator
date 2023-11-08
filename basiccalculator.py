n1 = float(input("Enter the 1st number: "))
operator = input("Enter the operator(+ - * /): ")
n2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = n1 + n2
    print(result)
elif operator == "-":
    result = n1 - n2
    print(result)
elif operator == "*":
    result = n1 * n2
    print(result)
elif operator == "/":
    result = n1 / n2
    print(result)
else: 
    print(f"{operator} is not valid")