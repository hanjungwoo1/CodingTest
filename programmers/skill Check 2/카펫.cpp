#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    
    int total = brown + yellow;
    int left, right;
    
    for(int i =3; i<total; i++){
        if (total % i == 0){
            left = total / i;
            right = i;
            
            if (left>= right){
                
                int yellow_count = (left - 2) * (right - 2);
                
                if (yellow_count == yellow){
                    answer.push_back(left);
                    answer.push_back(right);
                    return answer;
                }
                
            }
            
        }
    }
    
    return answer;
}