#program to calculate emi
p=int(input("Enter Principle amount:"))
t=int(input("Enter No.of Months:"))
r=int(input("Enter rate of interest"))
si=p*t*r/100
print("The Emi need to pay for Month:",(si+p)/12)
