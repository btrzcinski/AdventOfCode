f = open("Day1.txt")
data = f.read()
f.close()

floor = 0
pos = 1
entered_basement = -1
for c in data:
    if c == '(': floor += 1
    if c == ')': floor -= 1

    if floor == -1 and entered_basement == -1: entered_basement = pos
    pos += 1

print(entered_basement)
print(floor)
