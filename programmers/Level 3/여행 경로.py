from collections import defaultdict

def solution(tickets):
    path = []

    # 1. {시작점: [도착점리스트]} 형태로 그래프 생성
    graph = defaultdict(list)
    for (start, end) in tickets:
        graph[start].append(end)

    # 2. 도착점 리스트를 역순 정렬
    for airport in graph.keys():
        graph[airport].sort(reverse=True)

    # 3. 출발지는 항상 ICN이므로 stack에 먼저 넣어두기
    stack = ["ICN"]
    # 4. DFS로 모든 노드 순회
    while stack:
        # 4-1. 스택에서 가장 위의 저장된 데이터 꺼내오기
        top = stack.pop()

        # 4-2. top이 그래프에 없거나, top을 시작점으로 하는 티켓이 없는 경우 path에 저장
        if top not in graph or not graph[top]:
            path.append(top)
        # 4-3. top을 다시 스택에 넣고 top의 도착점 중 가장 마지막 지점을 꺼내와 스택에 저장
        else:
            stack.append(top)
            stack.append(graph[top].pop())

    # 5. path를 뒤집어서 반환
    return path[::-1]