VERTICES_NUM, EDGES_NUM = map(int, input().split())
answer = 0

graph = [
    [0 for _ in range(VERTICES_NUM + 1)]
    for _ in range(VERTICES_NUM + 1)
]

visited = [False for _ in range(VERTICES_NUM + 1)]

def  dfs(vertex):
    global answer
    for curr_v in range(1, VERTICES_NUM + 1):
        if graph[vertex][curr_v] and not visited[curr_v]:
            # print(curr_v)
            answer += 1
            visited[curr_v] = True
            dfs(curr_v)

for _ in range(EDGES_NUM):
    src, dst = map(int, input().split())
    graph[src][dst] = 1
    graph[dst][src] = 1

visited[1] = True
dfs(1)

print(answer)