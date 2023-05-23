#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

/*
투포인터 문제

정렬하고

합이 작으면 올리고, 높으면 내리고
target을 찾아 나간다.
*/ 



int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int num, a, target;
	cin >> num;
	vector<int> v;
	for (int i = 0; i < num; i++) {
		cin >> a;
		v.push_back(a);
	}
	cin >> target;
	sort(v.begin(), v.end());
	int l = 0, r = num-1, cnt = 0;

	while (1) {
		if (l >= r) 
			break;
		int sum = v[l] + v[r];
		if (sum == target) {
			cnt++;
			l++;
			r--;
		}
		else if (sum < target)
			l++;
		else
			r--;
	}
	cout << cnt;
	return 0;
}