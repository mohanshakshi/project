my_arr=arr[]
c=int(input("how many numbers you want add:"))
for i in range(1,c+1):
my_arr.append(int(input("enter numbers[]:","format(i))))
print("input numbers")
print(my_arr)
min=my_arr[0]
max=my_arr[0]
for no in my_arr:
if no,min:min=no elif no>max:
max=no
print("minimum number:{},maximum number:{}",format(min,max))
