/*
숨바꼭질3

deque나 우선순위큐를 통해서 처리
https://jdselectron.tistory.com/58
*/


#include <iostream>
#include <queue>
#include <stdio.h>
#include <cstring> // memset
 
using namespace std;
 
#define MAX_SIZE 100000+1
 
int N, K;
bool visited[MAX_SIZE];
 
int bfs() {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
    q.push({ 0, N });
    visited[N] = true;
    while (!q.empty()) {
        int time = q.top().first;
        int x = q.top().second;
        q.pop();
 
        if (x == K) return time;
 
        if (x * 2 < MAX_SIZE && !visited[x * 2]) {
            q.push({ time, x * 2 });
            visited[x * 2] = true;
        }
 
        if (x + 1 < MAX_SIZE && !visited[x + 1]) {
            q.push({ time + 1, x + 1 });
            visited[x + 1] = true;
        }
 
        if (x - 1 >= 0 && !visited[x - 1]) {
            q.push({ time + 1 , x - 1 });
            visited[x - 1] = true;
        }
    }
}
 
int main() {
    scanf("%d %d", &N, &K);
    printf("%d\n", bfs());
    return 0;
}