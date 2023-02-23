#include <iostream>
using namespace std;

int N; // 실행 코드의 데이터 개수
int M; // 바이러스의 데이터 개수
int A[20000 + 10]; // 실행 코드의 데이터
int B[10 + 10]; // 바이러스의 데이터

int sol; // 정답


void Sort(int *a, int s, int e)
{
	int i, j;

	for (i=s; i<e; i++){
		for(j=i+1; j<=e; j++){
			if(a[i] > a[j]){
				int t = a[i];
				a[i] = a[j];
				a[j] = t;
			}
		}


	}

}


void InputData(void)
{
	int i;

	cin >> N >> M;

	for (i = 0; i < N; i++) {
		cin >> A[i];
	}

	for (i = 0; i < M; i++) {
		cin >> B[i];
	}
}

void OutputData(void)
{
	cout << sol;
}


int P[10+10];
int first = 1;

int Find(int start)
{
	int i;
	int min;

	if(first == 1){
		first=0;

		Sort(B, 0, M-1);

		min = B[0];
		for(i=0; i<M; i++){
			B[i] = B[i] -min;
		}
	}

	for (i = 0; i<M; i++){
		P[i] = A[start + i];
	}

	Sort(P, 0, M - 1);

	min = P[0];

	for(i=0;i<M;i++){
		P[i] = P[i] - min;
	}

	for (i = 0; i < M; i++) {
		if (B[i] != P[i]) return 0;
	}
	return 1;
}

void Solve(void)
{
	int i;

	for (i = 0; i <= N - M; i++) {
		sol += Find(i);
	}
}

int main(void)
{
	InputData(); // 입력

	Solve(); // 문제 해결

	OutputData(); // 출력

	return 0;
}
