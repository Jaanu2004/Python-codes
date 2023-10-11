
#write a program to check the whether student is pass or fail
'''
sno,sname,group,s1,s2,s3
pass constraint,marks should greater than or equal to 40,
if the condition is true,then print pass otherwise print fail
s1>=40
s2>=40
s3>=40
'''
sname=input('Enter student name:')
sno=int(input('Enter sno;'))
sgrp=input('Enter student group:')
s1=int(input('Enter sub-1 marks:'))
s2=int(input('Enter sub-2 marks:'))
s3=int(input('Enter sub-3 marks:'))
if(s1>=40 and s2>=40 and s3>=40):
   print('pass')
else:
    print('fail')