'''
:Multistage graph
    :Each stage is made up of nodes.
    :Find the minimum at each stage and move forward to the next stage
    :Formula
        G(stage, node) = { min(G(next_stage, current_connected_node) + G(next_stage, current_connected_node)) }
    :Approach
        :calculation starts from target node and moves on to the previous nodes untill it reaches the source node
'''


def shortestDist(graph):
    global INF
    # initialising an array which holds minimum values of each node (theoretically at each stage) from a set of nodes its directed to
    dist = [0] * N
    dist[N - 1] = 0
    '''
    :start  
        :(N-2) - leaving out the target node
    :stop
        :-1 - till it reaches the source node i.e, 0
    :step
        :-1 - calculate for each node
    '''
    for i in range(N - 2, -1, -1):
        dist[i] = INF
        for j in range(N):
            if graph[i][j] == INF:  # check if there is any path exists between nodes
                continue

            # get the minimum path of the nodes from a set of nodes its directed to
            dist[i] = min(dist[i], graph[i][j] + dist[j])

    # returning the first element since it holds the minimum path to reach the target node
    return dist[0]


N = 8
INF = 99999999
# Representation of graph
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
