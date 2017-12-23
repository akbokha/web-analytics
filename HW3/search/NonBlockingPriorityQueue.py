class NonBlockingPriorityQueue:
    def __init__(self, max_size):
        self.items = []
        self.max = max_size
        self.index = 0

    def push(self, item, priority):
        #heapq.heappush(self.items, (-priority, x))
        if len(self.items) < self.max:
            heapq.heappush(self.items, (-priority, self.index, item))
            self.index += 1
        else:
        # Equivalent to a push, then a pop, but faster
        #spilled_value =
            heapq.heappushpop(self.items, (-priority, self.index, item))
            self.index += 1

    def pop(self):
        return heapq.heappop(self.items)[-1]

    def empty(self):
        return not self.items

    def print_elements(self):
        result = []
        for i in self.items:
            result.append(i)
        return result