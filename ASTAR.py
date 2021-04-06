import BestFirstSearch
import math

# A* algo, use best first search with hersutic function as f=g+h
# h is Euclidean distance


def Astar(board, start, end):
    def g(node):
        return node.path_cost

    def h(node):
        dx = abs(node.state[0] - end[0])
        dy = abs(node.state[1] - end[1])
        return max(dx, dy)
    return BestFirstSearch.best_first_graph_search(board, start, end, f=lambda n: g(n)+h(n))
