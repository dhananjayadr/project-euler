#!/usr/bin/python

def sum_of_multiples():
    result = sum(n for n in range(1000) if n%3 == 0 or n%5 == 0)
    return result 

if __name__ == '__main__':
    print(sum_of_multiples())
