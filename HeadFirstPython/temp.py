a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
# def dedupe(items, key=None):
#     seen = set()
#     for item in items:
#         val = item if key is None else key(item)
#         if val not in seen:
#             yield item
#             seen.add(val)
# li=list(dedupe(a, key=lambda d: d['x']))
# print(li)

def myfunc(items,key=None):
    s=set()
    for item in items:
        val = item if key is None else key(item)
        if val  not in s:
            yield item
            s.add(val)
li=list(myfunc(a, key=lambda d: d['x']))
print(li)            
rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

import itertools 
import operator
r=sorted(rows,key=lambda x:x['date'])
for key , items in itertools.groupby(r,key=lambda x:x['date']):
    print(key)
    for x in items:
        print(x)