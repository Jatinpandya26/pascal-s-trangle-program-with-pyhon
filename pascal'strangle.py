"""
This is a Python Program to print the pascal’s triangle 
draw a input random integer
a python program by user id jatin268
"""

n=int(input())
print("Number of rows = ", n)
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
        print("thank,jatin")
    print()
