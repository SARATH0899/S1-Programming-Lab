#Experiment 29:
#A program to find the greatest common divisor (GCD) of two numbers:
#Declaring two variable to which the user inputs the two numbers:
Nmb1=int(input("Enter any positive number : "))
Nmb2=int(input("Enter any positive number : "))
if(Nmb1==Nmb2):
    print("The two numbers are the same. Please enter two different numbers")
elif(Nmb1<0 or Nmb2<0):
    print("The number entered is not a positive number")
elif(Nmb1>Nmb2):
    G=Nmb1%Nmb2
    K=Nmb2%G
    if(K==0):
        print("The Greatest Common Divisor of (",Nmb1,",",Nmb2,"is",G)
elif(Nmb2>Nmb1):
    G=Nmb2%Nmb1
    K=Nmb1%G
    if(K==0):
        print("The Greatest Common Divisor of (",Nmb1,",",Nmb2,"is",G)
else:
    print("(",Nmb1,",",Nmb2,") do not have a Greatest Common Divisor")

