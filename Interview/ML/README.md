### Machine Learning

#### Naive Bayes Classification



#### 지도 학습 VS 비지도 학습

- supervised Learning : labeled Data
- unsupervised Learning : not need labeled Data

#### Machine Learning VS Deep Learning

- Machine Learning : Input -> Feature Extraction -> Classification -> Output
- Deep Learning : Input -> Feature Extraction + Classification -> Output

#### Boosting VS Bagging

- Boosting
    - **sequential**
    - 처음 모델이 예측을 하면 그 결과에 따라 데이터에 가중치가 부여
    - 부여된 가중치가 다음 모델에 영향
    - 잘못 분류된 데이터에 집중하여 새로운 분류 규칙을 만드는 단계를 반복
    - XGBoost, LightGBM
- 
- Bagging: Bootstrap Aggregation
    - **parallel**
    - 복원 추출 방식으로 데이터를 추출하여 모델을 학습
    - 같은 과정을 여러번 반복하여 여러 개의 개별 학습 모델을 만듦
    - 학습 시킨 모델에 테스트 데이터가 입력된다면, 각 모델별로 예측 값을 만들고 투표(분류)나 평균(회귀)로 최종 예측
    - ex) 랜덤 포레스트


#### Confusion Matrix

- True Positive(TP) : 실제 True인 정답을 True라고 예측 (정답)
- False Positive(FP) : 실제 False인 정답을 True라고 예측 (오답)
- False Negative(FN) : 실제 True인 정답을 False라고 예측 (오답)
- True Negative(TN) : 실제 False인 정답을 False라고 예측 (정답)

- precision $$ TP/TP+FP $$

### PCA

### EDA

### Regularization

### Normalization

### Regression

### Tree VS Regression


