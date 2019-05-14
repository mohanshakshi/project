a=int(input("enter the first number:"))
b=int(input("enter  the second number:"))
n=int(input("enter the number of terms"))
print(a,b,end=' ')
while(n-2):
c=a+b
a=b
b=c
print(c,ends='  ')
n=n-1
