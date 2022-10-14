integers = [1,2,3,4,5,6]
odd_ints = []
squared_odds = []
total = 0
for i in integers:
    if i%2 == 1:
        odd_ints.append(i)
for i in odd_ints:
    squared_odds.append(i*i)
for i in squared_odds:
    total += i

print(squared_odds)
print(odd_ints)