def input_string_to_pystr(s):
    return eval(s)

def input_string_to_escaped_str(s):
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    return '"' + s + '"'

def main():
    with open("Day8.txt") as f:
        strings = [l.rstrip() for l in f.readlines()]
    
    num_chars_code = 0
    num_chars_memory = 0
    num_chars_encoded = 0
    for input_str in strings:
        num_chars_code += len(input_str)
        num_chars_memory += len(input_string_to_pystr(input_str))
        num_chars_encoded += len(input_string_to_escaped_str(input_str))
    
    print("code - memory = %d - %d = %d" % (num_chars_code, num_chars_memory, num_chars_code - num_chars_memory))
    print("encoded - code = %d - %d - %d" % (num_chars_encoded, num_chars_code, num_chars_encoded - num_chars_code))

if __name__ == "__main__":
    main()