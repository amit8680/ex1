import BestFirstSearch

# UCS algo, use best first search with hersutic function as f=g


def uniform_cost_search(board, start, end):
    def g(node):
        return node.path_cost
    return BestFirstSearch.best_first_graph_search(board, start, end, f=g)
