#include <iostream>
using namespace std;

int N;//협찬 물품의 수
int D[100000 + 10];//선호도
int sol = -30001;//첫번째 방법의 최대 선호도

void InputData(){
	cin >> N;
	for(int i=0;i<N;i++){
		cin >> D[i];
	}
}

void TwoPointer()
{
	int sum = 0;
	sol = -10001;

	for(int i=0; i<N; i++){
		if (sum >0){
			sum += D[i];
		}
		else{
			sum = D[i];
		}
		if (sol < sum){
			sol = sum;
		}
	}


}


int main(){
	InputData();//입력 함수
	//Solve();
	TwoPointer();
	cout << sol << endl;//출력
	return 0;
}