n=int(input())
temp=n
res=0
while n!=0:
    r=n%10
    n=n//10
    res=res+r**3
if res==temp:
    print('Armstrong number')
else:
    print('Not a Armstrong Number')
