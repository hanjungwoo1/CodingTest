/*
적록색약

DFS 맵바꿔가면서

*/

#include <stdio.h>
#include <string.h>

using namespace std;

int n, cnt = 0;
char photo[100][100];
bool isVisited[100][100] = { false };

int dx[4] = { 0,0,-1,1 };
int dy[4] = { -1,1,0,0 };

void dfs(int x, int y) {
	isVisited[x][y] = true;
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
		if (!isVisited[nx][ny] && photo[x][y] == photo[nx][ny]) {
			dfs(nx, ny);
		}
	}
}

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", photo[i]);
	}

	//적록색약이 아닌 사람
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!isVisited[i][j]) {
				dfs( i, j);
				cnt++;
			}
		}
	}
	printf("%d ", cnt);

	//적록색약인 사람
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (photo[i][j] == 'G') photo[i][j] = 'R';
			else photo[i][j] = photo[i][j];
		}
	}
	memset(isVisited, false, sizeof(isVisited));

	cnt = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!isVisited[i][j]) {
				dfs(i, j);
				cnt++;
			}
		}
	}
	printf("%d", cnt);

	return 0;
}