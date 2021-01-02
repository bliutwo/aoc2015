strings = None
with open('input.txt') as f:
    strings = f.read()
assert(strings)
# print(strings)
strings = strings.split('\n')
total = 0
for line in strings:
    if line:
        dimensions = line.split('x')
        # print(dimensions)
        dimensions = [int(n) for n in dimensions]
        dimensions.sort()
        assert(len(dimensions) == 3)
        l, w, h = dimensions
        # print(l, w, h)
        surface_area = 2*l*w + 2*w*h + 2*h*l
        smallest = l*w
        # print(surface_area)
        # print(smallest)
        total += surface_area + smallest
        # print(total)
print(total)
