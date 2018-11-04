import json
from collections import defaultdict
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

path = 'ch02/usagov_bitly_data.txt'
records = [json.loads(line) for line in open(path)]
print(records[0])

time_zone = [rec['tz'] for rec in records if 'tz' in rec]

frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:10].plot(kind='barh', rot=0)

def get_conts(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

arr = np.array([1,2,3])
arr.astype(np.int32)