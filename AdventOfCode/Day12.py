import json

def sum_of_numbers_in_json(doc, exclude_red_objects=False):
    sum = 0
    def int_decoder(num):
        nonlocal sum
        sum += int(num)
        return int(num)
    def object_decoder(obj):
        if "red" in obj.keys() or "red" in obj.values():
            return {}
        return obj
    if exclude_red_objects:
        doc = json.dumps(json.loads(doc, object_hook=object_decoder))
    json.loads(doc, parse_int=int_decoder)
    return sum

def main():
    with open("Day12.txt") as f:
        input = f.read()
        print("Sum:", sum_of_numbers_in_json(input))
        print("Sum without 'red' objects:", sum_of_numbers_in_json(input, True))

if __name__ == "__main__":
    main()
