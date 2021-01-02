strings = None
with open('input.txt') as f:
    strings = f.read()
assert(strings)
# print(strings)
strings = strings.split('\n')
total = 0
ribbon = 0
for line in strings:
    if line:
        dimensions = line.split('x')
        dimensions = [int(n) for n in dimensions]
        dimensions.sort()
        assert(len(dimensions) == 3)
        l, w, h = dimensions
        surface_area = 2*l*w + 2*w*h + 2*h*l
        smallest = l*w
        total += surface_area + smallest
        wrap = l + l + w + w
        bow  = l*w*h
        ribbon += wrap + bow
print(total)
print(ribbon)
