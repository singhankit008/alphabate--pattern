for row in range(11):
    for col in range(12):
        if (col==0 or col==11)  or ((row==0 or row==6) and (col>0 and col<11)):
            print("A",end="")
        else:
            print(end=" ")
    print()
