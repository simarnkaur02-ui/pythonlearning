a = int(input(" Enter a number between 1 and 10: "))

match a:
    case 1:
        print(" You won a car")
    case 3:
        print(" you won a $ 8")
    case 6:
        print(" you won a laptop")
    case _:
        print("Better luck next time")    
       
        