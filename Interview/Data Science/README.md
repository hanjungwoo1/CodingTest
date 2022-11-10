# Data Science

## Pandas

<details>
<summary>Click</summary>

#### 

```python
import pandas as pd

df = pd.read_csv("")

# Remove duplicated elements
df.duplicated().sum()

# Fix the typo
df.rename(columns={"Handcap": "Handicap"}, inplace=True)

# Change the data type
df.AppointmentDay = pd.to_datetime(df.AppointmentDay).dt.date
df.ScheduledDay = pd.to_datetime(df.ScheduledDay).dt.date

# 'No-show'를 'Show'로 바꾸겠습니다. 또한 Yes는 0, No는 1로 데이터
df.rename(columns={"No-show": "Show"}, inplace=True)
df.replace({'Show': {'No': 1, 'Yes': 0}}, inplace = True)

# Modify nonsense values -> 음수 불허
df[df['PeriodBetween'] < 0] = 0

# Segment PeriodBetween values into bins
bins = pd.IntervalIndex.from_tuples([(-1, 1), (1, 5), (5, 10), (10, 200)])
labels=["rightNow", "fewDaysAgo", "severalDaysAgo", "longAgo"]
df['PeriodBetween'] = pd.cut(df['PeriodBetween'], bins=bins, labels=labels)
```
</details>

## 데이터의 종류(양적 데이터, 질적 데이터)

<details>
<summary>Click</summary>

<table>

<tr>
    <td colspan="2">양적 데이터 (Quantitative, Numeric)<br>: 수학 연산을 할 수 있는 수치 값</td>
    <td colspan="2">질적 데이터 (Qualitative, Categorical)<br>:범주로 나누어지는 값</td>
</tr>

<tr>
    <td> 연속형 (Continuos) </td>
    <td>ex) 키, 나이, 수입</td>
    <td> 순서형 (Ordinal) </td>
    <td> Grade, 순위(랭킹) </td>
</tr>

<tr>
    <td> 이산형 (Discrete) </td>
    <td>ex) 사과의 갯수, 책의 페이지 수 </td>
    <td> 명목형 (Nominal) </td>
    <td> 성별, 뷔페의 음식 메뉴, 우편 번호 </td>
</tr>

</table>            

</details>

## 기술 통계학과 추측 통계학

<details>
<summary>Click</summary>

### 통계학의 구분

- 기술 통계학(Descriptive Statistics)과 추측 통계학(Inferential Statistics)으로 구분
- 기술 통계 : 현재 가지고 있는 데이터를 기반
- 추측 통계 : 현재 가지고 있는 데이터로부터 더 큰 집단의 특징을 추측(확률론)

### 기술 통계학

정량적(Quantative) 데이터를 기술하는 4가지 방법

- 대표값(Center) : 평균(Mean), 중앙값(Median), 최빈값(Mode)
- 흩어짐 정도(Spread) : 범위(Range), 사분위 간 범위(Interquatile Range, IQR), 분산(Variance), 표준편차(Standard Deviation)
- 분포 형태(Shape of distribution) : Symmetric (주로 정규분포), Right-skewed, Left-skewed
- 극단치(Outliers)

### 추측 통계학

- 모집단(Population) : 관심 있는 대상 모두의 수치적 자료
- 모수(Parameter) : 모집단의 특징을 나타내는 양적인 측도
- 표본(Sample): 모집단으로부터 뽑은 부분집합
- 통계량(Statisctic): 표본의 특성을 나타내는 양적인 측도
- 표본의 통계량 -> 모집단의 모수를 추론

</details>


## 분산과 표준편차에서 n이 아니라 n-1로 나누는 이유(자유도)

<details>
<summary>Click</summary>

### 자유도(Degree of freedom)

- 평균 = (x1 + x2 + x3 + ... + x(n-1) + x(n)) / n
- 마지막은 정해져있기 때문에 n-1로 나누어야 한다

### 분산과 표준편차를 구할 때 n이 아닌 n-1로 나누는 이유는?

- 표본 분산은 모 분산보다 작은 경향
- 모 분산보다 작아지려는 경향을 가진 표본 분산을 보존
- n으로 나눈 표본 분산보다 n-1로 나눈 표본 분산 값이 더 클 것

</details>


## reference

- https://bkshin.tistory.com/entry/DATA-6