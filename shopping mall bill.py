##shopping mall bill with christmas and sankranthi offers
kurti=150
saree=500
shirt=300
pant=250
nightsuit=190
print('****************Welcome To Jahnavi Fashions*****************')
cname=input('Enter Customer Name:')
cph=input('Enter Customer Phone Number:')
kq=int(input("Enter No.of.Kurtis purchased:"))
sq=int(input("Enter No.of.sarees purchased:"))
shq=int(input("Enter No.of.shirts purchased:"))
pq=int(input("Enter No.of.pants purchased:"))
nq=int(input("Enter No.of.nightsuits purchased:"))
off=input('Enter offer Name')
bill=(kurti*kq)+(saree*sq)+(shirt*shq)+(pant*pq)+(nightsuit*nq)
if off=='christmas' or off=='CHRISTMAS':
    dis=bill*40/100
elif off=='Sankranthi' or off=='SANKRANTHI':
    dis=bill*50/100
elif bill>=2000:
    dis=bill*20/100
elif bill>=1000:
    dis=bill*10/100
elif bill>=500:
    dis=bill*5/100
else:
    dis=bill*3/100
tbill=bill-dis
gst=tbill*12/100
obill=tbill+gst
print('Customer Name:',cname)
print('Customer Phone Number:',cph)
print('bill:',bill)
print('Discount:',dis)
print('Gst 12%:',gst)
print('Bill to be Paid:',obill)
print('*******************Thank you !!!! Vist Again***************')

    
