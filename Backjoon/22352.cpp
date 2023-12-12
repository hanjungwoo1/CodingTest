/*
항체 인식

BFS, 다른 위치 찾아서 한번 돌리고
bf, af를 파라미터로 같이 넘겨줘서
그 값으로 바꾸는 형태로 짜야한다.
*/


#include <iostream>
#include <queue>
using namespace std;
int bef[32][32];
int aft[32][32];
int dx[] = {0, 0, -1, 1};
int dy[] = {1, -1, 0, 0};
int n, m;
 
void bfs(int a,int b,int bf, int af){
    queue<pair<int, int>> q;
    q.push(make_pair(a, b));
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
 
        for (int i = 0; i < 4;i++){ //상하좌우로 움직임
            int nx = x + dx[i];
            int ny = y + dy[i];
 
            if(nx < m && nx >=0 && ny <n && ny >=0){              
                if(bef[ny][nx] == bf){ // 바뀌어야할 값이면
                    bef[ny][nx] = af; // 결과 값으로 바꾸어 줌
                    q.push(make_pair(nx, ny)); 
                }
            }
        }
    }
}
 
int main(){
    ios::sync_with_stdio(false);
    cin >> n >> m;
    
    for (int i = 0; i < n;i++){
        for (int j = 0; j < m;j++){
            cin >> bef[i][j]; //놓기 전 값
        }
    }
    for (int i = 0; i < n;i++){
        for (int j = 0; j < m;j++){
            cin >> aft[i][j]; // 놓은 후 값
        }
    }
    bool injected = false;
    for (int i = 0; i < n;i++){
        for (int j = 0; j < m;j++){
            if(!injected){ // 백신은 한번만 놓을 수 있음
                if(bef[i][j] != aft[i][j]){
                    bfs(j, i, bef[i][j], aft[i][j]);
                    bef[i][j] = aft[i][j]; // 첫 시작 값 바꾸어줌
                    injected = true;
                }
            }
        }
    }    
    for (int i = 0; i < n;i++){
        for (int j = 0; j < m;j++){
            if(bef[i][j] != aft[i][j]){ // 하나라도 다르면 NO
                cout << "NO"; 
                return 0;
            }
        }
    }
    cout << "YES";
    return 0;
} //25min