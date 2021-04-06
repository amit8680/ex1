import Node
import sys
import math

count = 0


# ida* algo that revice the problem as arguments
# board- 2d array,start/end-the start/end point on board


def iterative_deepening_Astar(board, start, end):
    global count
    root = Node.Node(start)
    # cost function for nodes


# Heuristics function


    def h(node):
        dx = abs(node.state[0] - end[0])
        dy = abs(node.state[1] - end[1])
        return max(dx, dy)

    def costf(node):
        return h(node)+node.path_cost
    fLimit = costf(root)
    while 1:
        result, fLimit = DFSc(root, fLimit, start, end, board, costf)
        if result:
            return result.solution(), result.path_cost, count
        # sys.maxsize used as inifinty
        if fLimit == sys.maxsize:
            return None

# Recursive function that return the flimit of every iteration


def DFSc(node, fLimit, start, end, board, costf):
    global count
    if costf(node) > fLimit:
        return None, costf(node)
    if node.state == end:
        return node, fLimit
    count = count+1
    nextF = sys.maxsize
    for child in node.expand(board):
        if child.depth == 20:
            return None, nextF
        res, newF = DFSc(child, fLimit, start, end, board, costf)
        if res:
            return res, fLimit
        nextF = min(newF, nextF)
    return None, nextF
