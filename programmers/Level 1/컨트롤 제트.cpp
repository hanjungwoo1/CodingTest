#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cctype>

using namespace std;

int solution(string s) {
    int answer = 0;
    int temp = 0;

    istringstream ss(s);
    string stringBuffer;
    vector<string> words;

    while (getline(ss, stringBuffer, ' ')){
        words.push_back(stringBuffer);
    }

    for(int i =0; i<words.size(); i++){
        if(words[i]=="Z")
            answer -= stoi(words[i-1]);
        else{
            answer += stoi(words[i]);
        }
    }

    return answer;
}