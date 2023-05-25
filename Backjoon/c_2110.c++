/*
공유기 설치

이진탐색

IDEA : 제일 작은 값, 제일 큰 값 

MIN, MAX로 둔다 (2대 설치)
이진 탐색으로 (Middle 마다 설치)

answer = min(abs(MIN - MIDDLE), abs(MAX-MIDDLE));

*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	int n, c, num, st, router, start, end, mid, ans = 0;
	cin >> n >> c;
	vector<int> pos;
	for (int i = 0; i < n; i++)
	{
		cin >> num;
		pos.push_back(num);
	}
	sort(pos.begin(), pos.end());
	start = 1;                             // 최소 거리
	end = pos[n - 1] - pos[0];             // 최대 거리

	while (start <= end)
	{
		router = 1;
		mid = (start + end) / 2;
		st = pos[0];

		for (int i = 1; i < n; i++)
		{
			if (pos[i] - st >= mid)
			{
				router++;
				st = pos[i];
			}
		}

		if (router >= c)
		{
			ans = max(ans, mid);
			start = mid + 1;
		}

		else
			end = mid - 1;
	}
	cout << ans;
	return 0;
}
