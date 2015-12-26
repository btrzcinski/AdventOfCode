def n_from_row_col(row, col):
    n = 1 + sum(range(row))
    n += sum(range(row+1, col+row))
    return n

# Adapted from https://en.wikipedia.org/wiki/Modular_exponentiation
def modexp(base, exp, mod):
    if mod == 1: return 0
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return result

def code_for_n(n):
    return (20151125 * modexp(252533, n - 1, 33554393)) % 33554393

def code_for_row_col(row, col):
    return code_for_n(n_from_row_col(row, col))

def main():
    with open("Day25.txt") as f:
        l = f.readline().strip().split()
        col = int(l[-1].strip("."))
        row = int(l[-3].strip(","))

    print("Code for row=%d, col=%d: %d" % (row, col, code_for_row_col(row, col)))

if __name__ == '__main__':
    main()
