str1=''
for row in range(14):
    for col in range(12):
        if ((col==0 or col==11) and row!=0) or ((row==0 or row==8) and (col>0 and col<11)):
            str1 = str1 + "A"
        else:
            str1 = str1 + " "
    str1 = str1 + "\n"
print(str1,end=" ")

str2=""
for row in range(10):
    for col in range(7):
        if(col==0)or (col==6 and(row!=0 and row!=5 and row!=9 )) or ((row==0 or row==5 or row==9) and (col>0 and col<6)):
            str2= str2 + "*"
        else:
            str2 = str2 + " "
    str2 = str2 + "\n"
print(str2)