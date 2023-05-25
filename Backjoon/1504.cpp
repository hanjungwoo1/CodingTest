/*
특정한 최단 경로

두 경로를 무조건 들렸다 가는 최단 경로 문제

다익스트라를 통해서
1에서 시작한 도착 위치 거리
v1에서 시작한 도착 위치 거리
v2에서 시작한 도착 위치 거리

sTov1 + v1tov2 + v2toN
sTov2 + v2tov1 + v1toN
중에 짧은 거리를 선택
*/
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>
using namespace std;
const int INF = 987654321;
int N, E, v1, v2, res = INF;
int sToV1, sToV2, V1ToV2, V1ToN, V2ToN;
vector<pair<int, int>> v[801]; // v[a] = (b,c) : a에서 b까지 c의 거리로 이동 가능
int dist[801];

void dijk(int start)
{
	for (int i = 0; i <= N; i++) dist[i] = INF;
	dist[start] = 0;
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
	q.push({ 0,start }); // 현재까지 거리, 현재 위치
	while (!q.empty()) {
		int cur = q.top().second;
		int curDist = q.top().first;
		q.pop();
		for (int i = 0; i < v[cur].size(); i++) {
			int next = v[cur][i].first;
			int nextDist = v[cur][i].second;
			if (dist[next] > curDist + nextDist) {
				dist[next] = curDist + nextDist;
				q.push({ dist[next],next });
			}
		}
	}
}

int main()
{
	cin >> N >> E;
	while (E--) {
		int a, b, c;
		cin >> a >> b >> c;
		v[a].push_back({ b,c });
		v[b].push_back({ a,c });
	}
	cin >> v1 >> v2;

	dijk(1);
	sToV1 = dist[v1];
	sToV2 = dist[v2];

	dijk(v1);
	V1ToV2 = dist[v2];
	V1ToN = dist[N];

	dijk(v2);
	V2ToN = dist[N];


	res = min(res, sToV1 + V1ToV2 + V2ToN);
	res = min(res, sToV2 + V1ToV2 + V1ToN);
	if (V1ToV2 == INF || res == INF) cout << -1;
	else cout << res;
}