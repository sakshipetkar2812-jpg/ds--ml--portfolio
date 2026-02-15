num_1=int(input("Enter first number: "))
num_2=int(input("Enter second number"))
choice=input("Choose one operations....*,-,+,/ : ")

if choice == "*":
    print("Output: ",num_1*num_2)
elif choice == "-":
    print("Output: ",num_1-num_2)
elif choice =="+":
    print("Output: ",num_1+num_2)
elif choice == "/":
    if num_2 != 0:
        print("Output: ",num_1/num_2)
    else:
        print("Cannot divide by 0")
else:
    print("Please enter valid input")



