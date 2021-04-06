import heapq

# taken from leacther's github


class PriorityQueue:
    def __init__(self, f=lambda x: x):
        self.heap = []
        self.f = f
        self.counter = 0

    def append(self, item):
        self.counter += 1
        heapq.heappush(self.heap, (self.f(item), self.counter, item))

    def extend(self, items):
        for item in items:
            self.append(item)

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[2]
        else:
            raise Exception('Trying to pop from empty PriorityQueue.')

    def __len__(self):
        return len(self.heap)

    def __contains__(self, key):
        return any([item == key for _, _, item in self.heap])

    def __getitem__(self, key):
        for value, _, item in self.heap:
            if item == key:
                return value
        raise KeyError(str(key) + " is not in the priority queue")

    def __delitem__(self, key):
        try:
            del self.heap[[item == key for _, _,
                           item in self.heap].index(True)]
        except ValueError:
            raise KeyError(str(key) + " is not in the priority queue")
        heapq.heapify(self.heap)

    def __repr__(self):
        return str(self.heap)
