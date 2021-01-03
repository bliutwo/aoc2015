import hashlib

# takes a secret key and produces the lowest number
# it combines with to produce an MD5 hash starting with
# at least five zeroes
def produce_answer(secret_key):
    for i in range(100000000):
        to_check = secret_key + str(i)
        result = hashlib.md5(to_check.encode())
        str_result = result.hexdigest()
        if len(str_result) >= 5 and str_result[0:5] == "00000":
            print(i)
            return str(i)
    print("not found")
    return -1

actual_input = "iwrupvqb"

samples_and_answers = {"abcdef": "609043", "pqrstuv": "1048970"}

for sample, answer in samples_and_answers.items():
    print(produce_answer(sample) == answer)

print(produce_answer(actual_input))
