str1=''
for row in range(10):
    for col in range(6):
        if ((col==0 and row!=9) or (col==5 and row!=9))or (row==9 and (col>0 and col<5)):
            str1= str1 + "U"
        else:
            str1= str1+" "
    str1= str1 +"\n"
print(str1 )