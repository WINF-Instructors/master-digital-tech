from functools import reduce
integers = [1,2,3,4,5,6]
odd_ints = list(filter(lambda n: n % 2 == 1, integers))
squared_odds = list(map(lambda n: n * n, odd_ints))
total = reduce(lambda acc, n: acc + n, squared_odds)

print(squared_odds)
print(odd_ints)