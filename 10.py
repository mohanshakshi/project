def sumKrepeating(arr,n,k):
sum=0
visited=[false for i in range(n)]
for i in range (0,n,):
if(visited[i]==true)
continue
count=1
for j in range(i+,n,):
if(arr[i]==arr[j]):
count+=
visited[j]=true
if (count==k):
sum+=arr[i]
return sum
if__name__=='__main__':
arr=[9,9,10,8,8,9,8]
n=len(arr)
k=3
print(sumKRepeating(arr,n,k))
