import numpy as np

symbols = {
    "#":3,
    "&":5,
    "@":7,
    "$":9,
    "★":1
}

win_symbols=["&","#","★"]

values=[]

for symb in symbols:
    values.append(symbols[symb])

print(values)
value=np.average(values)

print(value)