def lowest_numbered_house_to_get_presents(num_presents, elf_house_limit=None, elf_gift_multiplier=10):
    houses = [0] * ((num_presents // elf_gift_multiplier) // 2)
    lowest_index = len(houses)
    for elf_num in range(1, len(houses)+1):
        if elf_house_limit is None: elf_house_max = len(houses)
        else: elf_house_max = min(len(houses), (elf_num-1) + (elf_num * elf_house_limit))
        for house_index in range(elf_num-1, elf_house_max, elf_num):
            houses[house_index] += (elf_num * elf_gift_multiplier)
            if houses[house_index] >= num_presents and house_index < lowest_index:
                lowest_index = house_index
    return lowest_index + 1

def main():
    input_num = 29000000
    print("Part 1:", lowest_numbered_house_to_get_presents(input_num))
    print("Part 2:", lowest_numbered_house_to_get_presents(input_num, elf_house_limit=50, elf_gift_multiplier=11))


if __name__ == '__main__':
    main()