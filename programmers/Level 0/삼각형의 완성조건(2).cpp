#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> sides) {
    int answer = 0;
    int max = *max_element(sides.begin(), sides.end());
    int min = *min_element(sides.begin(), sides.end());

    // max가 가장 큰변
    for(int i = 0; i < max+1; i++){
        if (i + min > max){
            //cout << i << endl;
            answer += 1;
        }
    }

    // left가 가장 큰변
    for(int j = max+1; j < max*2+1; j++){
        if (min+max > j){
            //cout << j << endl;
            answer += 1;
        }
    }

    return answer;
}