/*
트리

1. 루트 노드부터 탐색하며 찾은 자식은, 루트를 맵핑하는 형태
2. 루트를 모른다면 지속으로 탐색하면서 자식이 두 가지이면, 그 노드는 루트 -> 맵핑을 지운다
*/

#include <iostream>
#include <vector>

using namespace std;
#define MAX 100001

int N;
int arr[MAX];
bool visited[MAX];
vector<int> v[MAX];

void dfs(int k) {
    visited[k]=true;
    for(int i=0;i<v[k].size();i++) {
        int next = v[k][i];
        if(!visited[next]) {
            arr[next]=k;
            dfs(next);
        }
    }
}

int main() {
    cin >> N;

    for(int i=0;i<N;i++) {
        int x,y;
        cin >> x >> y;
        v[x].push_back(y);
        v[y].push_back(x);
    }

    dfs(1);

    for(int i=2;i<=N;i++) cout << arr[i] << "\n";
}
