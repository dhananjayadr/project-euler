#!/usr/bin/python

def largest_prime_fractor(num):
    result = []
    for i in range(2, int((num)**(1/2))+1):
        if num % i == 0 and isPrime(i):
            result.append(i)
        else:
            continue 
    return None if len(result) == 0 else max(result)

def isPrime(n):
    if n > 1:
        for i in range(2, int((n)**(1/2))+1):
            if n % i == 0:
                return False
                break
        else:
            return True

    else:
        return False

if __name__ == '__main__':
    print(largest_prime_fractor(600851475143))
