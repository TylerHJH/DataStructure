import random
import time


def take_out_coffee_can(n, m):
    b = n
    w = m
    while b + w != 0:
        p = random.randint(1, b + w)
        if p <= b:
            b -= 1
        else:
            w -= 1
        print('black:', b, 'white:', w)


start = time.process_time()
take_out_coffee_can(5, 5)
end = time.process_time()
print(end - start)
