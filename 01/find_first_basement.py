filename = "input.txt"
paren_string = None
with open(filename) as f:
    paren_string = f.read()
assert(paren_string)
# print(paren_string)
floor = 0
for i, c in enumerate(paren_string):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    if floor == -1:
        print(i+1)
        break
