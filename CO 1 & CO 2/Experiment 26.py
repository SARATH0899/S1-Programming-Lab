#Experiment 26:
#A program to check whether a number is Fibonacci or not
#Declaring a variable to which the user inputs the required number:
Nmb=int(input("Enter the required number: "))
i=0
j=1
k=1
if(Nmb==0 or Nmb==1):
    print(Nmb,"is a fibonacci number")
else:
    while(i<Nmb):
        i=j+k
        k=j
        j=i
    if(i==Nmb):
        print(Nmb,"is a fibonacci number")
    else:
        print(Nmb,"is not a fibonacci number")
