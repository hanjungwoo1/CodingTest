#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
 
#define INF 1e9+7
#define ull unsigned long long
 
using namespace std;
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, tmp;
    ull ans = 0;
    int isSame = 0;
    cin >> n;
    stack<pair<int, int>> s;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        while (!s.empty() && s.top().first <= tmp) {
            if (s.top().first == tmp) {
                isSame = s.top().second;
                ans += s.top().second;
                s.pop();
            }
            else ans+=s.top().second, s.pop();
        }
        if (s.size() > 0)    ans++;
        if (isSame)    s.push({ tmp, isSame + 1 });
        else s.push({ tmp, 1 });
        isSame = 0;
    }
    cout << ans;
}
