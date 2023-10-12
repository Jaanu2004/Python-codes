sname=input('Enter Student Name:')
sno=int(input('Enter Student No:'))
sgrp=input('Enter Student Group:')
s1=int(input('Enter Sub-1 marks:'))
s2=int(input('Enter Sub-2 marks:'))
s3=int(input('Enter Sub-3 marks:'))
total=s1+s2+s3
avg=(s1+s2+s3)/3
if avg>=90:
    print('O-Grade')
elif avg>=80:
    print('A-Grade')
elif avg>=70:
    print('B-Grade')
elif avg>=60:
    print('C-Grade')
elif avg>=50:
    print('D-Grade')
else:
    print('pass')



