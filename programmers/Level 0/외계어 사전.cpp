#include <string>
#include <vector>

using namespace std;

int arr[26];
int check[26];

int solution(vector<string> spell, vector<string> dic) {
    int answer = 2;

    for(int i=0; i<spell.size(); i++)
        arr[spell[i][0]-'a']=1;

    for(int i=0; i<dic.size(); i++){
        int cnt=0;
        for(int j=0; j<dic[i].size(); j++){
            if(arr[dic[i][j]-'a']==1 && check[dic[i][j]-'a']==0) {
                check[dic[i][j]-'a']=1;
                cnt++;
            }

            else break;
        }

        if(cnt==spell.size()){
            answer=1;
            break;
        }

        for(int j=0; j<26; j++)
            check[j]=0;
    }

    return answer;
}