#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

template<typename K, typename V>
void print_map(std::unordered_map<K, V> const &m)
{
    for (auto const &pair: m) {
        std::cout << "{" << pair.first << ": " << pair.second << "}\n";
    }
}


vector<int> solution(string s) {
    vector<int> answer;
    unordered_map<char, int> umap;

    for(int i=0; i< s.length(); i++){
        if(umap.find(s[i]) !=umap.end()){
            int index = umap[s[i]];
            answer.push_back(i-index);
            umap[s[i]] = i;
        }else{
            answer.push_back(-1);
            umap[s[i]] = i;
        }
        // print_map(umap);
        // cout << "end\n";
    }

    return answer;
}