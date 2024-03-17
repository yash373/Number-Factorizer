def factorize(n):
    factors = []
    i = 2

    while n > 1:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    
    return factors

if __name__ == '__main__':
    print(factorize(int(input("Enter Number to Factorize: "))))