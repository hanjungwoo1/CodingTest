/*
두 용액

정렬
target과 가까우면 저장
마지막 출력

*/

#include <iostream>
#include <vector>
#include <algorithm>
#define INF 2000000000
using namespace std;

vector<int> answer(2);
int main() {
    int N;
    cin >> N;
    vector<int> arr(N);
    for (int i = 0; i < N; ++i)
        cin >> arr[i];
    sort(arr.begin(), arr.end()); // 정렬 필수!

    int start = 0; // start 은 왼쪽 끝에서
    int end = N - 1; // end 은 오른쪽 끝에서 시작
    int min = INF; // 현재까지 0 에 가장 가까웠던 합
    while (start < end) {
        int sum = arr[start] + arr[end];

        if (min > abs(sum)) {
            min = abs(sum);
            answer[0] = arr[start];
            answer[1] = arr[end]; 

            if (sum == 0)
                break;
        }

        if (sum < 0) 
            start++;
        else 
            end--;
    }

    cout << answer[0] << " " << answer[1];
}