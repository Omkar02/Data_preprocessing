from collections import defaultdict
from  Labler import myList_lable
import numpy as np


source = myList_lable

def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return ((key,locs) for key,locs in tally.items()
                            if len(locs)>1)

for dup in sorted(list_duplicates(source)):
    #print('Indexing:', dup)
    label, values = dup
    end_values = np.max(values) + 1
    start_value = end_values - 2032
    print('Y','[',start_value,':',end_values,']','=',label)
