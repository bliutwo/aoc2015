strings = None
with open('input.txt') as f:
    strings = f.read()
assert(strings)
strings = strings.split('\n')
strings = strings[:-1]

print(strings[-1])
