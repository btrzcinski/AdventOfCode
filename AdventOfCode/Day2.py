global boxdata
with open("Day2_input.txt") as f:
    boxdata = f.readlines()

total_paper = 0
total_ribbon = 0
for box in boxdata:
    l,w,h = [int(x) for x in box.rstrip().split("x")]
    side1,side2,side3 = l*w,w*h,h*l
    total_paper += 2*side1 + 2*side2 + 2*side3 + min(side1, side2, side3)
    total_ribbon += sum([2*x for x in sorted([l,w,h])[0:2]]) + l*w*h

print("Wrapping paper sq ft: %d" % (total_paper,))
print("Ribbon ft: %d" % (total_ribbon,))
