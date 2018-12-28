str1=""
for row in range(10):
    for col in range(7):
        if (col==0 and (row!=0 and row!=1 and row!=2 and row!=3 and row!=4 and row !=5)) or (col==6 and row!=9) or(row==9 and (col>0 and col<6)):
            str1 = str1 + "J"
        else:
            str1= str1 + " "
    str1 = str1 +'\n'
print(str1)    