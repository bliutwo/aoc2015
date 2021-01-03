vowels = {'a', 'e', 'i', 'o', 'u'}
naughty_strings = {"ab", "cd", "pq", "xy"}

def three_vowels(name):
    vowel_count = 0
    for c in name:
        if c in vowels:
            vowel_count += 1
    return vowel_count >= 3

def twice_in_a_row(name):
    n = len(name)
    for i in range(1, n):
        if name[i] == name[i - 1]:
            return True
    return False

def no_naughty_strings(name):
    n = len(name)
    for i in range(2, n):
        if name[i-2:i] in naughty_strings:
            return False
    return True

# takes a name and returns whether it is nice or naughty
def is_nice(name):
    return three_vowels(name) and twice_in_a_row(name) and no_naughty_strings(name)

samples_and_solutions = {
    "ugknbfddgicrmopn": True,
    "aaa": True,
    "jchzalrnumimnmhp": False,
    "haegwjzuvuyypxyu": False,
    "dvszwmarrgswjxmb": False
}

for name, niceness in samples_and_solutions.items():
    print(is_nice(name) == niceness)

strings = None
with open('input.txt') as f:
    strings = f.read()
assert(strings)
strings = strings.split('\n')
strings = strings[:-1]

nice_count = 0

for name in strings:
    if is_nice(name):
        nice_count += 1

print(nice_count)
