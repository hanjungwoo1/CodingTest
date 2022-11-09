## Machine Learning

### Naive Bayes Classification

<details>
<summary>Click</summary>


- 나이브 베이즈는 스팸 메일 필터, 텍스트 분류, 감정 분석, 추천 시스템 등에 광범위하게 활용되는 분류 기법
- feature끼리 서로 독립이라는 조건이 필요
- [ref](https://bkshin.tistory.com/entry/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-1%EB%82%98%EC%9D%B4%EB%B8%8C-%EB%B2%A0%EC%9D%B4%EC%A6%88-%EB%B6%84%EB%A5%98-Naive-Bayes-Classification)

</details>

### SVM, Support Vector Machine

<details>
<summary>Click</summary>

- 경계선(Decision Boudary) : Margin을 최대화하는 선을 생성 
- Robustness : outlier의 영향을 받지 않는다.

#### Kernel Trick

- Kernel Trick : 저차원 공간(low dimensional Space)을 고차원 공간(High dimensional Space)으로 매핑해주는 작업
- ![kernel_trick](images/Kernel_Trick.PNG)

#### Kernel, C, Gamma

- Kernel : decision boundary 모양 (linear, poly, sigmid, rbf)
- C : 크면 overfitting(굴곡), 낮으면 underfitting(직선)
- Gamma : Defines how far the influence of a single training point reaches 
  - Gamma 작으면 reach가 멀다, Gamma 높으면 reach가 가깝다
  - Gamma 크다 -> reach 가깝다 -> 멀리있는 것 영향 X -> 굴곡
  - Gamma 작다 -> reach 멀다 -> 대부분 영향 -> 잘 안구부러 짐

</details>

### 결정 트리, Decision Tree

<details>
<summary>Click</summary>

- 분류, 회귀 모두 가능
- ![decision_tree](images/decision_tree.PNG)
- 지나치게 많이 하면 오버피팅이 된다

#### 가지치기, Pruning

- 오버피팅을 막기 위한 전략
- min_sample_split : 한 노드에 들어있는 최소 데이터 수

#### 알고리즘 : 엔트로피(Entropy), 불순도(Impurity)

- 불순도 : 해당 범주 안에 서로 다른 데이터가 얼마나 섞여 있는지
- 엔트로피 : 불순도를 수치적으로 나타낸 척도. 
- 엔트로피가 1이면 불순도가 최대(WORST), 엔트로피가 0이면 불순도는 최소(BEST)

- ![entropy](images/entropy.PNG)


#### 정보 획득(Information gain)

- 엔트로피가 1인 상태에서 0.7인 상태로 바뀌었다면 정보 획득(information gain)은 0.3
- Information gain = entropy(parent) - [weighted average]entropy(children)
- 결정 트리 알고리즘은 정보 획득을 최대화하는 방향으로 학습이 진행됩니다. 


</details>

### 랜덤 포레스트, Random Forest

<details>
<summary>Click</summary>

- jj
- jj


</details>


### 지도 학습 VS 비지도 학습

- supervised Learning : labeled Data
- unsupervised Learning : not need labeled Data

### Machine Learning VS Deep Learning

- Machine Learning : Input -> Feature Extraction -> Classification -> Output
- Deep Learning : Input -> Feature Extraction + Classification -> Output

### Boosting VS Bagging

<details>
<summary>Click</summary>


- Boosting
    - **sequential**
    - 처음 모델이 예측을 하면 그 결과에 따라 데이터에 가중치가 부여
    - 부여된 가중치가 다음 모델에 영향
    - 잘못 분류된 데이터에 집중하여 새로운 분류 규칙을 만드는 단계를 반복
    - XGBoost, LightGBM

- Bagging: Bootstrap Aggregation
    - **parallel**
    - 복원 추출 방식으로 데이터를 추출하여 모델을 학습
    - 같은 과정을 여러번 반복하여 여러 개의 개별 학습 모델을 만듦
    - 학습 시킨 모델에 테스트 데이터가 입력된다면, 각 모델별로 예측 값을 만들고 투표(분류)나 평균(회귀)로 최종 예측
    - ex) 랜덤 포레스트

</details>

### Confusion Matrix

<details>
<summary>Click</summary>


![confusion_matrix](images/confusion_matrix.PNG)

    True Positive(TP) : 실제 True인 정답을 True라고 예측 (정답)
    False Positive(FP) : 실제 False인 정답을 True라고 예측 (오답)
    False Negative(FN) : 실제 True인 정답을 False라고 예측 (오답)
    True Negative(TN) : 실제 False인 정답을 False라고 예측 (정답)


#### Precision, Recall and Accuracy

- Precision 
  - ![precision](images/precision.PNG)
- Recall
  - ![recall](images/recall.PNG)
- Trade-off
  - Precision과 Recall은 Trade-OFF 관계
  - FN, FP의 Trade-OFF -> Precision과 Recall

#### Accuracy and F1-Score

- Accuracy
  - ![accuracy](images/accuracy.PNG)

- F1-Score
  - F1 score는 Precision과 Recall의 조화평균
  - ![F1-Score](images/F1-score.PNG)
  - 조화평균 : 산술평균과 다르게 큰 비중이 끼치는 bias를 줄이는 방식
  - ![F1-Score2](images/F1-score_2.PNG)

</details>


### 

### PCA

### EDA

### Regularization

### Normalization

### Regression

### Tree VS Regression

