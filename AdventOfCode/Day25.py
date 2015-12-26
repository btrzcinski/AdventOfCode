def n_from_row_col(row, col):
    n = 1 + sum(range(row))
    n += sum(range(row+1, col+row))
    return n

def code_for_n(n):
    code = 20151125 # start
    for _ in range(1, n):
        code *= 252533
        code %= 33554393
    return code

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
