num = int(input("Enter a number Between 1 to 7: "))

match num:
    case 1:
        print("SUNDAY")

    case 2:
        print("MONDAY")

    case 3:
        print("TUESDAY")

    case 4:
        print("WEDNESDAY")

    case 5:
        print("THURSDAY")
   
    case 6:
        print("FRIDAY")

    case 7:
        print("SATURDAY")    
     
    case _:
        print("please enter a vaild number")

