#include <string>
#include <vector>

using namespace std;

int solution(string my_string) {
    int answer = 0, n=0;

    for(int i=0; i<my_string.size(); i++){
        if(isdigit(my_string[i])){
            n=n*10+my_string[i]-'0'; // 연속이면 n이 있는 숫자라 *10
        } else {
            answer+=n;
            n=0;
        }
    }

    answer+=n;

    return answer;
}