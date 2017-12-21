import heapq
from heapq import heappush, heappop

class priority_queue:
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


def phiSet(desc):

def phiYule(Set):

def constraints(descList):
    return len(descList) > 20

def phiEntropy(Set):

def beam_search(d, w, q, qualityFunc, satisfies, refinement, desclist):
    candidateQueue = []
    resultSet = priorityMax(q)
    for level in range(0, d):
        beam = priorityMax(w)
        while candidateQueue.not_empty:
            seed = candidateQueue.get()
            set_refined = refinement(seed)
            for desc in set_refined:
                quality = phiYule(desc)
                if desc.satisfiesAll(C):
                    resultSet.put(desc.quality)
                    beam.put(desc.quality)
            while beam.not_empty:
                candidateQueue.put(beam.get())
    return resultSet

result = beam_search(d=2, w=5, q=5, qualityFunc = phiYule, satisfies = constraints, refinement, df)
result
