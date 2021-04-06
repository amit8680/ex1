# Node class- represent every node in our search problem
# node contains state-the curret position on board,
# parent-the node the came befor in the path,path cost until now and
# depth in path till now
class Node:
    # constractor
    def __init__(self, state, parent=None, action="", path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
    # Returns a list of all nodes that can be developed
    # in a step from the current node according to the terms
    #

    def expand(self, board):
        Nodes = []
        if self.state[1] < len(board)-1:
            if board[self.state[0]][self.state[1]+1] != -1:
                Nodes.append(Node((self.state[0], self.state[1]+1),
                                  self, "R", self.path_cost+board[self.state[0]][self.state[1]+1]))
        if self.state[0] < len(board)-1 and self.state[1] < len(board)-1:
            if board[self.state[0]+1][self.state[1]+1] != -1 and board[self.state[0]][self.state[1]+1] != -1 and board[self.state[0]+1][self.state[1]] != -1:
                Nodes.append(Node((self.state[0]+1, self.state[1]+1),
                                  self, "RD", self.path_cost+board[self.state[0]+1][self.state[1]+1]))
        if self.state[0] < len(board)-1:
            if board[self.state[0]+1][self.state[1]] != -1:
                Nodes.append(Node((self.state[0]+1, self.state[1]),
                                  self, "D", self.path_cost+board[self.state[0]+1][self.state[1]]))
        if self.state[0] < len(board)-1 and self.state[1] > 0:
            if board[self.state[0]+1][self.state[1]-1] != -1 and board[self.state[0]+1][self.state[1]] != -1 and board[self.state[0]][self.state[1]-1] != -1:
                Nodes.append(Node((self.state[0]+1, self.state[1]-1),
                                  self, "LD", self.path_cost+board[self.state[0]+1][self.state[1]-1]))
        if self.state[1] > 0:
            if board[self.state[0]][self.state[1]-1] != -1:
                Nodes.append(Node((self.state[0], self.state[1]-1),
                                  self, "L", self.path_cost+board[self.state[0]][self.state[1]-1]))
        if self.state[0] > 0 and self.state[1] > 0:
            if board[self.state[0]-1][self.state[1]-1] != -1 and board[self.state[0]-1][self.state[1]] != -1 and board[self.state[0]][self.state[1]-1] != -1:
                Nodes.append(Node((self.state[0]-1, self.state[1]-1),
                                  self, "LU", self.path_cost+board[self.state[0]-1][self.state[1]-1]))
        if self.state[0] > 0:
            if board[self.state[0]-1][self.state[1]] != -1:
                Nodes.append(Node((self.state[0]-1, self.state[1]),
                                  self, "U", self.path_cost+board[self.state[0]-1][self.state[1]]))
        if self.state[0] > 0 and self.state[1] < len(board)-1:
            if board[self.state[0]-1][self.state[1]+1] != -1 and board[self.state[0]][self.state[1]+1] != -1 and board[self.state[0]-1][self.state[1]] != -1:
                Nodes.append(Node((self.state[0]-1, self.state[1]+1),
                                  self, "RU", self.path_cost+board[self.state[0]-1][self.state[1]+1]))
        return Nodes

    # return all action from the start until the end
    def solution(self):
        return [node.action for node in self.path()[1:]]
    # return full path from start to end

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __repr__(self):
        return f"<{self.state}>"

    def __lt__(self, node):
        return self.state < node.state

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self.state)
