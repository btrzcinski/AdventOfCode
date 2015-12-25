from collections import defaultdict
from difflib import SequenceMatcher
from operator import itemgetter
from time import sleep

def replacements_for_molecule(molecule, before, after):
    index = molecule.find(before)
    while index > -1:
        yield molecule[0:index] + after + molecule[index+len(before):]
        index = molecule.find(before, index + 1)

def generated_molecules_from_molecule(molecule, replacement_map):
    for replacement in replacement_map:
        for after in replacement_map[replacement]:
            for replacement_molecule in replacements_for_molecule(molecule, replacement, after):
                yield replacement_molecule

def steps_to_get_molecule(target_molecule, replacement_map):
    return 0

def main():
    replacement_map = defaultdict(list)
    with open("Day19.txt") as f:
        lines = f.readlines()
        target_molecule = lines[-1].strip()
        for map_line in lines[:-2]:
            before, _, after = map_line.strip().split(" ")
            replacement_map[before].append(after)
    generated_molecules = set(generated_molecules_from_molecule(target_molecule, replacement_map))
    print("Distinct molecules:", len(generated_molecules))
    steps = steps_to_get_molecule(target_molecule, replacement_map)
    print("Fewest number of steps:", steps)

if __name__ == '__main__':
    main()