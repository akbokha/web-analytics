import csv
from HW3.search.NonBlockingPriorityQueue import NonBlockingPriorityQueue

def parsecsv(path):
    file = open(path)
    reader = csv.reader(file)
    data = []
    attributes = []
    for index, row in enumerate(reader):
        row = list(map(lambda x: None if x == '' else x, row))
        if index == 0:
            for col in row:
                attributes.append((col, set()))
        else:
            data.append(row)
            for i, col in enumerate(row):
                attributes[i][1].add(col)
    attributes = list(map(lambda x: (x[0], list(x[1])), attributes))
    return data, attributes
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
