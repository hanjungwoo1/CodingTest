/*
섬의 개수

BFS, Flood Fill

for문 중첩으로 i,j를 visit처리해서
Flood Fill 시작할 수 있는 위치 갯수 세기
*/

// 섬의 개수(BFS)
// 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
#include <iostream>
#include <cstring>
#include <queue>
using namespace std;
queue<pair<int,int>>Q;
int map[50][50],visit[50][50];
int dx[8]={1,1,0,-1,-1,-1,0,1},dy[8]={0,1,1,1,0,-1,-1,-1};
int w,h;
void bfs(){
    while(!Q.empty()){
        int y=Q.front().first;
        int x=Q.front().second;
        Q.pop();
        for(int i=0;i<8;i++){
            int nextY=y+dy[i];
            int nextX=x+dx[i];
            if(nextX<0||nextY<0||nextX>=w||nextY>=h)continue;
            if(map[nextY][nextX]&&!visit[nextY][nextX]){
                Q.push({nextY,nextX});
                visit[nextY][nextX]=1;
            }
        }
    }
}
int main(){
    ios_base::sync_with_stdio(0);cin.tie(NULL);
    while(1){
        int cnt=0;
        cin>>w>>h;
        if(!w&&!h)break;
        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                cin>>map[i][j];
            }
        }
        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                if(!visit[i][j]&&map[i][j]){
                    Q.push({i,j});
                    visit[i][j]=1;
                    bfs();
                    cnt++;
                }
            }
        }
        cout<<cnt<<"\n";
        memset(visit,0,sizeof(visit));
    }
}