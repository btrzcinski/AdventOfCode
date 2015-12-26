from itertools import combinations
from operator import itemgetter

def list_prod(l):
    prod = 1
    for m in l: prod *= m
    return prod

# returns: ([grp1], [grp2], [grp3]<, [grp4]>)
def valid_groups(package_list, grp1_size, best_only=False, group_num=3):
    best_qe = 10000000000000
    for grp1 in combinations(package_list, grp1_size):
        divisor_check = 2 + (group_num - 3)
        if (sum(package_list) - sum(grp1)) / divisor_check != sum(grp1): continue
        if best_only and list_prod(grp1) > best_qe: continue
        grp234 = [p for p in package_list if p not in grp1]
        grp2_size_subtractor = 1 + (group_num - 3)
        for grp2_size in range(1, len(grp234) - grp2_size_subtractor):
            for grp2 in combinations(grp234, grp2_size):
                if sum(grp2) != sum(grp1): continue
                if group_num == 3:
                    grp3 = [p for p in grp234 if p not in grp2]
                    if best_only: best_qe = min(best_qe, list_prod(grp1))
                    yield (list(grp1), list(grp2), grp3)
                else:
                    grp34 = [p for p in grp234 if p not in grp2]
                    for grp3_size in range(1, len(grp34) - 1):
                        for grp3 in combinations(grp34, grp3_size):
                            if sum(grp3) != sum(grp2): continue
                            grp4 = [p for p in grp34 if p not in grp3]
                            if best_only: best_qe = min(best_qe, list_prod(grp1))
                            yield (list(grp1), list(grp2), list(grp3), grp4)

def best_groups(package_list, group_num=3):
    found_grp1_size = False
    grp1_size_subtractor = 2 + (group_num - 3)
    for grp1_size in range(1, len(package_list) - grp1_size_subtractor):
        print("best_groups: trying grp1_size = %d" % grp1_size)
        for g in valid_groups(package_list, grp1_size, best_only=True, group_num=group_num):
            found_grp1_size = True
            yield g
        if found_grp1_size: return

def best_qe(package_list, group_num=3):
    min_qes = 10000000000000
    best_group = None
    try:
        for g in best_groups(package_list, group_num):
            qes = list_prod(g[0])
            if qes < min_qes:
                min_qes = qes
                best_group = g
                print("New best QE: %d, %s" % (min_qes, repr(best_group)))
    except KeyboardInterrupt:
        print("Stopping early, keyboard interrupt")
    return (min_qes, best_group)

def main():
    package_list = []
    with open("Day24.txt") as f:
        for l in f:
            package_list.append(int(l.strip()))
    print("Packages:", package_list)
    print("3-Group:", best_qe(package_list))
    print("4-Group:", best_qe(package_list, 4))

if __name__ == '__main__':
    main()