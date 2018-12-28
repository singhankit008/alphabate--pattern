str1=""
for row in range(10):
    for col in range(7):
        if (col==0 and(row!=0 and  row !=9)) or ((row==0 or row==9) and (col>0 and col<7)):
            str1= str1+ "#"
        else:
            str1 = str1 + " "
    str1= str1 + '\n'
print(str1)