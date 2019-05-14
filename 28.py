using namespace std;
void reorder(int arr[], int index[], int n0
{
int temp[n]:
for (int i=0; i<n; i++)
temp[index[i]]=arr[i];
for (int i=0; i<n; i++)
{
arr[i] =temp[i]:
index[i]=i;
}
}
int main()
{
int arr[]={67,98,98,76};
int index[]=[3,8,9,8};
int n=sizeof(arr)/sizeof(arr[0]);
reorder(arr,index,n);
cout<<"reordered array is :\n";
for (int i=0; i<n; i++)
cout<< arr[i]<< "  ";
cout<<"\nModified index array is :\n";
for(int i=0; i<n; i++)
cout<< index[i]<< "  ";
return 0;
