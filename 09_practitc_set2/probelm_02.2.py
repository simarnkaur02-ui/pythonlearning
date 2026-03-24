num1 = int(input("enter first number"))
num2 = int(input("enter second number"))

operation = input("choose operation")

match operation:
      case "+":
            print(num1 + num2)
      case "-":
            print(num1 - num2)
      case "*":
            print(num1 * num2)
      case "/":
            print(num1 / num2)

