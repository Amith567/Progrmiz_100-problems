run=True
while run:
    print("1.add\n2.sub\n3.mul\n4.div")
    choice=int(input("enter your choice : "))
    operand_1=int(input('enter first operand : '))
    operand_2=int(input('enter second operand : '))
    if choice==1: 
        print(f"result {operand_1+operand_2}")
    elif choice==2:
        print(f"result {operand_1-operand_2}")
    elif choice==3:
        print(f"result {operand_1*operand_2}")
    elif choice==4:
        print(f"result {operand_1/operand_2}")
    else:
        print("invalid choice")
    next=input('do you want to continue : (y/n) ')
    run=(next=='y')


    