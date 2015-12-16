from collections import defaultdict

def new_aunt_map():
	return defaultdict(lambda: defaultdict(lambda: None))

def get_aunt_map_from_file(filename):
	aunt_map = new_aunt_map()
	with open(filename) as f:
		for line in f:
			_, sue_num, attr1, val1, attr2, val2, attr3, val3 = line.strip().replace(":","").replace(",","").split()
			aunt_map[int(sue_num)][attr1] = int(val1)
			aunt_map[int(sue_num)][attr2] = int(val2)
			aunt_map[int(sue_num)][attr3] = int(val3)
	return aunt_map	

def best_match_for_candidate(aunt_map, aunt_candidate, greater_keys=[], lessthan_keys=[]):
	best_matches = 0
	best_aunt = 0
	for aunt in aunt_map:
		aunt_data = aunt_map[aunt]
		equality_keys = [k for k in aunt_data.keys() if k not in (greater_keys + lessthan_keys)]
		equality_matches = len([k for k in equality_keys if aunt_candidate[k] == aunt_data[k]])
		greater_matches = len([k for k in greater_keys if aunt_data[k] is not None and aunt_data[k] > aunt_candidate[k]])
		lessthan_matches = len([k for k in lessthan_keys if aunt_data[k] is not None and aunt_data[k] < aunt_candidate[k]])
		matches = equality_matches + greater_matches + lessthan_matches	
		if matches > best_matches:
			best_matches, best_aunt = matches, aunt
	return best_aunt	

def main():
	aunt_map = get_aunt_map_from_file("Day16.txt")
	aunt_candidate = {
		'children': 3,
		'cats': 7,
		'samoyeds': 2,
		'pomeranians': 3,
		'akitas': 0,
		'vizslas': 0,
		'goldfish': 5,
		'trees': 3,
		'cars': 2,
		'perfumes': 1
	}
	best_match_one = best_match_for_candidate(aunt_map, aunt_candidate)
	print("Best match, part one:", best_match_one)
	best_match_two = best_match_for_candidate(aunt_map, aunt_candidate, greater_keys=["cats", "trees"], lessthan_keys=["pomeranians", "goldfish"])
	print("Best match, part two:", best_match_two)

if __name__ == "__main__":
	main()
