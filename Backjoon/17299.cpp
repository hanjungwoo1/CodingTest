#include <cstdio>
#include <stack>
using namespace std;

int n;
int F[1000001], ans[1000001], nums[1000001];
stack<int> st;
int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &nums[i]);
		F[nums[i]]++;
	}

	for (int i = n - 1; i >= 0; i--) {
		int number = nums[i];
		int height = F[number];
		while (!st.empty()) {
			int topNum = nums[st.top()];
			int topHeight = F[topNum];
			if (height >= topHeight) st.pop();
			else break;
		}
		ans[i] = -1;
		if (!st.empty()) ans[i] = nums[st.top()];
		st.push(i);
	}
	for (int i = 0; i < n; i++)
		printf("%d ", ans[i]);
	printf("\n");

}