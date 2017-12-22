import heapq

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


def phiSet(desc):

def phiYule(Set):

def constraints(desc_list):
    return len(desc_list) > 20

def phiEntropy(Set):

def beam_search(d, w, q, qualityFunc, satisfies, refinement, desclist):
    candidate_queue = []
    result_set = NonBlockingPriorityQueue(q)
    for level in range(0, d):
        beam = NonBlockingPriorityQueue(w)
        while candidate_queue.not_empty:
            seed = candidate_queue.get()
            set_refined = refinement(seed)
            for desc in set_refined:
                quality = phiYule(desc)
                if desc.satisfiesAll(C):
                    result_set.put(desc.quality)
                    beam.put(desc.quality)
            while beam.not_empty:
                candidate_queue.put(beam.get())
    return result_set

result = beam_search(d=2, w=5, q=5, qualityFunc = phiYule, satisfies = constraints, refinement, df)
result
