using namespace std;
void Nminelements(vector<int>list1,int N)
{
vector<int>final_list;
int n=list1.size();
for (int i =0;,i<N;i++)
{
int min1=99999999;
for (int j=0;j<n;
{
if(list1[j]<min1
min1=list1[j]
}
list1.erase(remove(list1.begin(),
list1.end(),min1)
list1.end());
}
for(int i=0; i<final_list_size();i++)
cout<<final+list<<"  ";
}
int main()
{
vector<int> list={6,87,98,87,98,65,567};
int N=2;
Nminelements(list1.N);
}
