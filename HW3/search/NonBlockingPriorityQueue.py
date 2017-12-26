class NonBlockingPriorityQueue:
    def __init__(self, max_size):
        self.items = []
        self.max = max_size

    def push(self, item, priority):
        if len(self.items) < self.max:
            heapq.heappush(self.items, (priority, item))
        else:
            heapq.heappushpop(self.items, (priority, item))

    def pop(self):
        return heapq.heappop(self.items)

    def get_max_item(self):
        return self.items[0]

    def empty(self):
        return not self.items

    def print_elements(self):
        result = []
        for i in self.items:
            result.append(i)
        return result

    def heap_sort(self):
        return [heapq.heappop(self.items) for _ in range(len(self.items))]