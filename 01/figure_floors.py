filename = "input.txt"
paren_string = None
with open(filename) as f:
    paren_string = f.read()
assert(paren_string)
# print(paren_string)
floor = 0
for c in paren_string:
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
print(floor)
