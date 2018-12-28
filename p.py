str1=''
for row in range(10):
    for col in range(7):
        if (col==0) or (col==6 and ( row!=6 and row!=7 and row!=8 and row!=9 )) or ((row==0 or row==5) and (col>0 and col<6)):
            str1= str1 +"P"
        else:
            str1 = str1+ " "
    str1 = str1 + '\n'
print(str1 )

str2=''
for row in range(10):
    for col in range(6):
        if ((col==0 and row!=9) or (col==5 and row!=9))or (row==9 and (col>0 and col<5)):
            str2= str2 + "U"
        else:
            str2= str2+" "
    str2= str2 +"\n"
print(str2 )
str3=""
for row in range(10):
    for col in range(7):
        if (col==0 and (row!=0 and row!=1 and row!=2 and row!=3 and row!=4 and row !=5)) or (col==6 and row!=9) or(row==9 and (col>0 and col<6)):
            str3 = str3 + "J"
        else:
            str3= str3 + " "
    str3 = str3 +'\n'
print(str3 )    
str4=''
for row in range(14):
    for col in range(12):
        if ((col==0 or col==11) and row!=0) or ((row==0 or row==8) and (col>0 and col<11)):
            str4 = str4 + "A"
        else:
            str4 = str4 + " "
    str4 = str4 + "\n"
print(str4)
