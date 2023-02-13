#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(string t, string p) {
    int answer = 0;
    int pLen = p.length();

    // init
    int tLen = t.length();
    string temp = "";
    for(int i = 0; i < pLen; ++i) {
        temp += t[i];
    }
    long long cmpNumber = stoll(temp);
    if(cmpNumber <= stoll(p)) {
        answer += 1;
    }

    // after
    for(int i = pLen; i < tLen; ++i) {
        string str = temp.substr(1, temp.length());

        cout << str +"\n";

        str += t[i];
        temp.clear();
        temp = str;
        cmpNumber = stoll(temp);
        if(cmpNumber <= stoll(p)) {
            answer += 1;
        }
    }
    return answer;
}