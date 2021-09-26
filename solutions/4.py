#!/usr/bin/python

result = []
for x in range(100, 1000):
    for y in range(100, 1000):
        temp = x * y
        if str(temp) == str(temp)[::-1]:
            result.append(temp)
print(max(result))

