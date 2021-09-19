#!/usr/bin/python

def sum_of_even_fibonacci():
    result = 0
    a, b = 0, 1
    while b < 4000000:
        a, b = b, a+b
        if b%2 == 0:
            result += b
    return result

if __name__ == '__main__':
    print(sum_of_even_fibonacci())

