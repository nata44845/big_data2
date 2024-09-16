import csv
from functools import reduce


price_col = 1

def mapper(row):
    price = int(row[price_col].strip())
    return 1, price, None

def reducer(score1, score2):
    scores = []
    if score1[2] == None:
        n, mean, M2 = 0, 0.0, 0
        scores.append(score1[1])
    else:
        n, mean, M2 = score1
    scores.append(score2[1])

    for score in scores:
        n += 1
        delta = score - mean
        mean += delta / n
        M2 += delta * (score - mean)
    return n, mean, M2

dataset_path = 'AB_NYC_price.csv'

with open(dataset_path, "r", encoding='utf8') as file:
    reader = csv.reader(file)
    n, mean, M2 = reduce(reducer, map(mapper, reader))
    print(n, mean, (M2 / n) ** (1/2))
