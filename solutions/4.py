#!/usr/bin/python

result = 0
for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        temp = x * y
        if str(temp) == str(temp)[::-1] and temp > result:
            result = temp
            break

print(result)

