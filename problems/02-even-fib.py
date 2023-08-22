"""
Find the sum of all even fibonacci numbers less than four million
"""

def fib(limit=float('inf')):
    seq = [0, 1]
    while True:
        nextitem = sum(seq)
        if (nextitem > limit):
            return
        yield nextitem
        seq = [seq[1], nextitem]

def main(limit=4_000_000):
    fib_numbers = fib(limit)

    total = 0
    for i in fib_numbers:
        if i % 2 == 0:
            total += i
    return total

if __name__ == '__main__':
    print(main())
