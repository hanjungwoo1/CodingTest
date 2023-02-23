

## Vector

### 삽입

#### Front
```C++
vector<int> test = {1,2,3,4,5};
test.insert(test.begin(), 0); // push front
```

```C++
0
1
2
3
4
5
```

#### Back
```C++
vector<int> test = {1,2,3,4,5};
test.push_back(8); // push back
```
```C++
1
2
3
4
5
8
```

### 삭제
test.erase(test.end()-1, test.end());

### 정렬

```C++
vector<int> test = {5, 4, 3, 2, 1};
sort(test.begin(), test.end());
```

```C++
1
2
3
4
5
```