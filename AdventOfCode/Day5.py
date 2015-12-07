def num_vowels(s):
    vowels = "aeiou"
    return len([c for c in s if c in vowels])

def has_bad_substring(s):
    substrings = ["ab", "cd", "pq", "xy"]
    substrings_in_s = [s.find(su) for su in substrings if s.find(su) > -1]
    return len(substrings_in_s) > 0

def has_double_letter(s):
    letter_pairs = [s[x:x+2] for x in range(0,len(s)-1)]
    matching_letter_pairs = [p for p in letter_pairs if p[0] == p[1]]
    return len(matching_letter_pairs) > 0

def has_non_overlapping_repeating_letter_pair(s):
    letter_pairs = [s[x:x+2] for x in range(0,len(s)-1)]
    repeated_pairs = [p for p in letter_pairs if s.count(p) > 1]
    return len(repeated_pairs) > 0

def has_bookended_letter_trigram(s):
    trigrams = [s[x:x+3] for x in range(0,len(s) - 2)]
    bookended_trigrams = [t for t in trigrams if t[0] == t[2]]
    return len(bookended_trigrams) > 0

def part_1_is_nice_string(s):
    if num_vowels(s) < 3: return False
    if has_bad_substring(s): return False
    if not has_double_letter(s): return False
    return True

def part_2_is_nice_string(s):
    if not has_non_overlapping_repeating_letter_pair(s): return False
    if not has_bookended_letter_trigram(s): return False
    return True

def main():
    strings = []
    with open("Day5.txt") as f:
        strings = [s.rstrip() for s in f.readlines()]
    part_1_nice_strings = [s for s in strings if part_1_is_nice_string(s)]
    print("Part 1 nice strings: %d" % (len(part_1_nice_strings),))
    part_2_nice_strings = [s for s in strings if part_2_is_nice_string(s)]
    print("Part 2 nice strings: %d" % (len(part_2_nice_strings),))

if __name__ == "__main__":
    main()
