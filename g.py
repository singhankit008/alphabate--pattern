str1=""
for row in range(6):
    for col in range(5):
        if ((col==0) or (row==0 )or (row==5 and col!=3)or((row==4) and (col!=0 and col!=1 and col!=3)) or
            (row==3 and(col!=0 and col!=1))or ((col==4) and (row!=2 and row!=3 and row!=4 and row!=5))):
            str1 = str1 +"*"
        else: 
            str1= str1 + " "
    str1= str1+ '\n'
print(str1)


