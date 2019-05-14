using namespace std;
void sortit(int array[],int n)
{
for (int i=0; i<n;i++)
array[i]=i+1;
}
}
int main()
{
int array[]={43,9,87,76,89,65,4};
int n=sizeof(array)/sizeof(array[0]);
sortit(array,n);
for(int i=0;i<n;i++)
cout<<array[i]<<"  ";
}
