from queue import Queue, PriorityQueue

# Beam width
w = 0

# Beam depth
d = 0

# Result set size
q = 0


def beam_search():
    candidate_queue = Queue()
    result_set = PriorityQueue(q)
    for level in range(1, d):
        beam = PriorityQueue(w)
        while candidate_queue.not_empty:
            seed = candidate_queue.get()
            set = n(seed)
            for desc in set:
                quality = phi(desc)
                if desc.satisfiesAll(C):
                    result_set.put(desc.quality)
                    beam.put(desc.quality)
            while beam.not_empty:
                candidate_queue.put(beam.get())

def n():

def phi():


