number1=float(input("enter first number:"))
number2=float(input("enter second number:"))
number3=float(input("enter third number:"))
if(number>number2) and (number>number3):
largest=number1
elif(number2>number1) and (number2>number3):
largest=number2
else:
largest=number3
print("the largest number is",largest)
