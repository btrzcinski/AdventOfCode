import timeit

def lookandsay_on_list(input):
    result = []
    work = input.copy()
    while len(work) > 0:
        num = work.pop(0)
        count_num = 1
        while len(work) > 0 and work[0] == num:
            count_num += 1
            work.pop(0)
        result.append(count_num)
        result.append(num) 
    return result

def list_from_string(input):
    return [int(c) for c in input]

def string_from_list(input):
    return "".join([str(i) for i in input])

def lookandsay(input, reps=40):
    list_input = list_from_string(input)
    for x in range(reps):
        list_input = lookandsay_on_list(list_input)
    return string_from_list(list_input)

def main():
    t1 = timeit.timeit("""print("%s ==(40x)=> ... (len = %d)" % ("1113122113", len(lookandsay("1113122113", 40))))""", setup="from __main__ import lookandsay", number=1)
    print("(%.3fs)" % (t1,))
    t2 = timeit.timeit("""print("%s ==(50x)=> ... (len = %d)" % ("1113122113", len(lookandsay("1113122113", 50))))""", setup="from __main__ import lookandsay", number=1)
    print("(%.3fs)" % (t2,))    

if __name__ == "__main__":
    main()
