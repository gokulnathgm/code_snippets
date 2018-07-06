lst = [3,3,9,9,5]
result = []
start = 0
size = 3
while start < len(lst):
    result.extend(lst[x+start:x+start+size] for x in range(end - start - size + 1))
print result
