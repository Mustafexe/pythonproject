#Calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
    num1 = int(input("What's the first number?: "))
    is_it_last_number=False
    while not is_it_last_number:

        for symbol in operations:
            print(symbol)


        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        first_answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {first_answer}")
        check=input("Do you wanna go with previous number 'y' or 'n'").lower()
        if check=="n":
            is_it_last_number=True
            calculator()
        else:
            num1=first_answer
calculator()

