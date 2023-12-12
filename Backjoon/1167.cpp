/*
트리의 지름

각 정점에서, 왼쪽 오른쪽의 최대 길이

하나의 정점에서, 최대 거리를 찾은 다음 -> 그 정점에서 다시 최대 거리를 찾으면, 양쪽 끝 값이 나온다
*/

#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int v = 0;
vector <pair<int, int>> vec[100001];
int far = 0, far_val = 0;
bool visited[100001];


void dfs(int current, int sum) {
	if (sum > far_val) {
		far = current;
		far_val = sum;
	}

	for (int i = 0; i < vec[current].size(); i++) {
		int num = vec[current][i].first;
		if (visited[num] == 0) {
			visited[num] = 1;
			dfs(num, sum + vec[current][i].second);
		}
	}


}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
	
	//input
	cin >> v;
	for (int i = 1; i <= v; i++) { // 간선 개수만큼 반복
		int a = 0;
		cin >> a;
		int b = 0, bval = 0;
		while (1) {
			cin >> b;
			if (b == -1)
				break;
			cin >> bval;
			vec[a].push_back(make_pair(b, bval));
			vec[b].push_back(make_pair(a, bval));

		}
	}

	//1. 가장 먼 곳 찾기
	memset(visited, 0, sizeof(visited));
	visited[1] = 1;
	dfs(1, 0);
	//cout << "far " << far << endl;
	
	//2. 결과 도출하기
	int f = far;
	far = 0, far_val = 0;
	memset(visited, 0, sizeof(visited));
	visited[f] = 1;
	dfs(f, 0);

	cout << far_val << endl;
	return 0;
}