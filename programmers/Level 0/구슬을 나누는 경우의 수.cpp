#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(int balls, int share) {
    int answer = 0;

    vector<int> num(balls), perm(balls);
    for (int i = 0; i < balls; i++) {
        num[i] = i + 1;
    }
    for (int i = balls - share; i < balls; i++) {
        perm[i] = 1;
    }
    do {
        for(int i = 0; i < perm.size(); i++){
            if (perm[i] == 1){
                // printf("%d ", num[i]);
            }
        }

        // printf("\n");
        answer += 1;
    } while(next_permutation(perm.begin(), perm.end()));

    return answer;
}