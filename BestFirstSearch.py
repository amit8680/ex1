import PriorityQueue
import Node

# best first searcg algoritm, Best-first search is a search
#  algorithm which explores a graph by expanding the most
#  promising node chosen according to f function.


def best_first_graph_search(board, start, end, f):
    node = Node.Node(start)
    frontier = PriorityQueue.PriorityQueue(f)  # Priority Queue
    frontier.append(node)
    closed_list = set()
    count = 0
    while frontier:
        node = frontier.pop()
        if end == node.state:
            return node.solution(), node.path_cost, count
        count = count+1
        closed_list.add(node.state)
        for child in node.expand(board):
            if child.state not in closed_list and child not in frontier:
                frontier.append(child)
            elif child in frontier and f(child) < frontier[child]:
                del frontier[child]
                frontier.append(child)
    return None
