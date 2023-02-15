#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>

using namespace std;

int solution(vector<vector<int>> dots) {
    int answer = 0;
    int width = 0;
    int height = 0;
    int tmp_width, tmp_height;

    for (int i = 0; i<dots.size(); i++){
        for (int j =0; j<dots.size(); j++){
            tmp_width = dots[i][0] - dots[j][0];
            tmp_height = dots[i][1] - dots[j][1];

            if (abs(tmp_width) > width){
                width = abs(tmp_width);
            }

            if (abs(tmp_height) > height){
                height = abs(tmp_height);
            }
        }
    }

    cout << width << endl;
    cout << height << endl;
    answer = width * height;
    return answer;
}