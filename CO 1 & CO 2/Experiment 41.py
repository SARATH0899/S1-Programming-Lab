#Experiment 41
#A program to store a list of first names. Count the occurrences of ‘a’ within the list:
#Declaring a variable to which the user inputs the first names:
Lst=[]
Lst1=[]
count=0
s=int(input("Enter the number of people to be added to the list : "))
#Using loop to enter the elements into the list:
for i in range(s):
    e=(input("Enter the first names : "))
    Lst.append(e)
    Lst1=list(e)
    Ct=Lst1.count('a')
    count=count+Ct
print(count)


