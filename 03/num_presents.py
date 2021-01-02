string = None
with open('input.txt') as f:
    string = f.read()
string.replace('\n', '')

directions = {
    '^': (0, 1),
    'v': (0, -1),
    '>': (1, 0),
    '<': (-1, 0)
}

# strings = ['>', '^>v<', '^v^v^v^v^v']
# strings = ['^v', '^>v<', '^v^v^v^v^v']

# for string in strings:
seen = set()
loc_x, loc_y = 0, 0
r_loc_x, r_loc_y, = 0, 0
seen.add((loc_x, loc_y))
delivered = 1
who = 1
for c in string:
    if c != '\n':
        x, y = directions[c]
        if who == 1:
            loc_x += x
            loc_y += y
            if (loc_x, loc_y) not in seen:
                delivered += 1
                seen.add((loc_x, loc_y))
        else:
            r_loc_x += x
            r_loc_y += y
            if (r_loc_x, r_loc_y) not in seen:
                delivered += 1
                seen.add((r_loc_x, r_loc_y))
        who *= -1
print(delivered)
