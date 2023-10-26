n=int(input("Enter n value:"))#5
temp=n
res=0
while n!=0:
    r=n%10#5
    n=n//10#0
    res=res*10+r#res=res+r**3
print(res)
if res==temp:
    print('Palindrome')
else:
    print('Not a palindrome')
