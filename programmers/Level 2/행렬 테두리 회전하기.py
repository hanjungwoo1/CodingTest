def solution(rows, columns, queries):
    answer = []

    # form 만들기
    # 주어진 rows, columns값을 가지고 rows X columns 의 form 을 만들어줍니다.
    form = []
    num = 1;
    for i in range(rows):
        now = []
        for j in range(columns):
            now.append(num);
            num += 1;
        form.append(now);

    # queries를 하나씩 받아들여 회전을 진행시킵니다.
    for x1, y1, x2, y2 in queries:
        min_num = 9999999999999;  # 최소값을 담기 위한 변수입니다. 그냥 크게 설정을 하고싶었습니다..
        temp = form[x1 - 1][
            y2 - 1];  # 회전을 진행하다보면 해당 줄에서 벗어나는 값이 있게 되는데 그중에 한 값을 미리 담아두어 나머지 값들이 줄을 벗어나더라도 입력될 수 있는 빈 칸을 만들어 줍니다..?

        # top
        # 상단부분을 회전시켜줍니다.
        min_num = min(min(form[x1 - 1][y1 - 1:y2]), min_num)  # 상단부분의 값중에 min_num 보다 작은 값이 있다면 업데이트 시켜줍니다.
        form[x1 - 1][y1:y2] = form[x1 - 1][y1 - 1:y2 - 1];

        # left
        # 좌측부분을 회전시켜줍니다.
        for x in range(x1, x2):
            min_num = min(form[x][y1 - 1], min_num)  # 좌측부분의 값중에 min_num 보다 작은 값이 있다면 업데이트 시켜줍니다.
            form[x - 1][y1 - 1] = form[x][y1 - 1];

        # bottom
        # 하단부분을 회전시켜줍니다.
        min_num = min(min(form[x2 - 1][y1 - 1:y2]), min_num)  # 하단부분의 값중에 min_num 보다 작은 값이 있다면 업데이트 시켜줍니다.
        form[x2 - 1][y1 - 1:y2 - 1] = form[x2 - 1][y1:y2];

        # right
        # 우측부분을 회전시켜 줍니다.
        for x in range(x2 - 1, x1, -1):  # 우측 방향은 아래방향으로 숫자가 이동해야 하기 때문에 x 값을 감소하는 포문으로 해야 같은 값이 계속해서 들어가지 않게 됩니다.
            min_num = min(form[x - 1][y2 - 1], min_num)
            form[x][y2 - 1] = form[x - 1][y2 - 1];

        form[x1][y2 - 1] = temp;  # 마지막 빈칸에 담아두었던 temp 값을 넣어줍니다.

        answer.append(min(temp, min_num))  # 마지막으로 temp와 min_num을 비교하여 작은 값을 answer에 담아줍니다.

    # 이를 반복하여 answer를 찾아냅니다.
    return answer