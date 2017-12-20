from queue import Queue, PriorityQueue

# Beam width
w = 0

# Beam depth
d = 0

# Result set size
q = 0


def beam_search():
    candidateQueue = Queue()
    resultSet = PriorityQueue(q)
    for level in range(1, d):
        beam = PriorityQueue(w)
        while candidateQueue.not_empty:
            seed = candidateQueue.get()
            set = n(seed)
            for desc in set:
                quality = phi(desc)
                if desc.satisfiesAll(C):
                    resultSet.put(desc.quality)
                    beam.put(desc.quality)
            while beam.not_empty:
                candidateQueue.put(beam.get())

def n():

def phi():


