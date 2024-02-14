mat = [[0, 1, 1, 0],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [0, 1, 1, 0]]

visited = [0, 0, 0, 0]

def bfs(num: int):
    visited[num] = 1
    q = [num]
    while len(q) != 0:
        n = q.pop(0)
        print(n)
        for i in range(len(mat)):
            if mat[n][i] == 1 and visited[i] != 1:
                q.append(i)
                visited[i] = 1
    
bfs(0)
