import Node
import sys

count = 0

# depth serach with limit value of iteration


def depth_limited_search(board, start, end, limit):
    global count
    frontier = [(Node.Node(start))]
    while frontier:
        node = frontier.pop()
        if node.state == end:
            return node.solution(), node.path_cost, count
        count += 1
        if node.depth < limit:
            nodes = node.expand(board)
            for n in reversed(nodes):
                frontier.append(n)
    return None

# ida algorithm with problem element as arguments


def iterative_deepening_search(board, start, end):
    for depth in range(0, 20):
        result = depth_limited_search(board, start, end, depth)
        if result:
            return result
    return None
