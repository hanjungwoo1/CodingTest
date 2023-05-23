#include <iostream>
#include <vector>
using namespace std;
 
int N;
vector<int> arr, res;

// key값 이상인 수 중에서 가장 먼저 나온 수의 인덱스를 반환
int mylower_bound(vector<int>& arr, int key){
    int st = 0;
    int ed = arr.size()-1;
    
    int mid = ed;
    
    while(ed > st){
        int mid = (st + ed)/2;
        if(key > arr[mid]){
            st = mid+1;
        }
        else{
            ed = mid;
        }
    }
    return ed;
}
 
void solve(){
    int cnt = 1;
    res.push_back(arr[0]);
    for(int i = 1; i < N; i++){
        if(res.back() < arr[i]){
            res.push_back(arr[i]);
            cnt++;
        }
        else{
            int idx = mylower_bound(res, arr[i]);
            res[idx] = arr[i];
        }
    }
    
    cout << cnt;
}
 
int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N;
    arr.resize(N+1);
    for(int i = 0; i < N; i++){
        cin >> arr[i];
    }
    
    solve();
    
    return 0;
}
 