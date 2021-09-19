#!/usr/bin/python

def sum_of_multiples():
    result = 0
    for n in range(1000):
        if n%3 == 0 or n%5 == 0:
            result += n
    return result 

if __name__ == '__main__':
    print(sum_of_multiples())
