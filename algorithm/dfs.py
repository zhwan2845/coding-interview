mat = [[0, 1, 1, 0],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [0, 1, 1, 0]]

visited = [0, 0, 0, 0]

def dfs(num: int):
    visited[num] = 1
    print(num)
    for i in range(len(mat)):
        if mat[num][i] == 1 and visited[i] != 1:
            dfs(i)

dfs(0)
