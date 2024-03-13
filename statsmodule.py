import statistics as st

from statistics import median
from statistics import mode

result=st.mean([1,85.9,59.5])

print (result)

print("")


nolist=[11,59,56,82,90,85,59,71,71,90]

print(median(nolist))

print(mode(nolist))

print(st.variance(nolist))

print(st.stdev(nolist))