# this one doesn't do anything
import pandas as pd
h1 = pd.read_csv('/media/data/Projects/arbes-gha/garbes_a_hhid.csv')
h2 = pd.read_csv('/media/data/Projects/arbes-gha/garbes_a_hhid2.csv')
print h2.head()
print h1.head()
print h1.count, h2.count
h = h1.append(h2, ignore_index = True)
3500 - 4000
4500 - 5000

h.to_csv('/media/data/Projects/arbes-gha/garbes_a_hhid_all.csv', index=False)
print h
print h1[h1.duplicated(['hhid_duplicatesid_key']) == True]['hhid_key']
print h[h['hhid_key'].isnull()]
print h[h['hhid_key'] >=4000]

h = pd.read_csv('/media/data/Projects/arbes-gha/garbes_a_hhid_all.csv')
print h[h.duplicated(['hhid_key']) == True]['hhid_key']

df = h[h.duplicated(['hhid_key']) == True]
print df
df.to_csv('/media/data/Projects/arbes-gha/hhid_duplicates.csv', index = False)

d1 = pd.DataFrame(h1['hhid_key'].head())
d2 = pd.DataFrame(h2['hhid_key'].head())
1926 - 1971
d2['hhid_key'][2] = 2
print d2['hhid_key'][2]
d1['Site'] = d['NAME_0']
d2[1][1] = 1

d = d1.append(d2, ignore_index = True)
print d

import random
def rand(exclude):
    r = None
    while r in exclude or r is None:
         r = random.randrange(1,10)
    return r

print rand([1,3,9])

print random.sample([1,3,9], 2)