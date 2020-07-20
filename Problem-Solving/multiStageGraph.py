'''
:Multistage graph
    :Each stage is made up of nodes.
    :Find the minimum at each stage and move forward to the next stage
    :Formula
        G(stage, node) = { min(G(next_stage, current_connected_node) + G(next_stage, current_connected_node)) }

'''


def shortestDist(graph):
    global INF
    dist = [0] * N
    dist[N - 1] = 0

    for i in range(N - 2, -1, -1):
        dist[i] = INF
        for j in range(N):
            if graph[i][j] == INF:
                continue

            dist[i] = min(dist[i], graph[i][j] + dist[j])

    return dist[0]


N = 8
INF = 99999999

graph = [
    [INF, 1, 2, 5, INF, INF, INF, INF],
    [INF, INF, INF, INF, 4, 11, INF, INF],
    [INF, INF, INF, INF, 9, 5, 16, INF],
    [INF, INF, INF, INF, INF, INF, 2, INF],
    [INF, INF, INF, INF, INF, INF, INF, 18],
    [INF, INF, INF, INF, INF, INF, INF, 13],
    [INF, INF, INF, INF, INF, INF, INF, 2]
]

print(shortestDist(graph))
