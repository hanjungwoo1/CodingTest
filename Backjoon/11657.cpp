/*
타임머신

벨만포드알고리즘
*/
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
#define INF 2100000000 // 21억

int N, M;
int A, B, C;
int a, b;
long long dist[501];
bool cycle;
vector<pair<int, int>> v[501];

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie();

	cin >> N >> M;

	for (int i = 0; i < M; i++)
	{
		cin >> A >> B >> C;
		v[A].push_back({ B,C });
	}
	
	for (int i = 1; i <= N; i++)
		dist[i] = INF; // 모든 노드를 INF로 세팅

	dist[1] = 0; // 시작점 0으로 초기화
	
	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= N; j++)
		{
			for (int k = 0; k < v[j].size(); k++)
			{
				int next = v[j][k].first;
				int d = v[j][k].second;

				if (dist[j] != INF && dist[next] > dist[j] + d)
				{
					dist[next] = dist[j] + d;
					if (i == N) cycle = true;
				}
					
			}
		}

	if (cycle) cout << -1 << '\n';
	else
	{
		for (int i = 2; i <= N; i++)
			cout << (dist[i] != INF ? dist[i] : -1) << '\n';
	}

	
}