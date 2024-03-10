n=int(input("enter number between 3-9"))
if(n<3 or n>9):
    print("wrong input")
else:
    for i in range(1, n + 1):
        print("*" * i)
    for i in range(n-1, 0, -1):
        print("*" * i)



