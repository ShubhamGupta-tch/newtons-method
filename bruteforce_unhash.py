from string_hash import hash_str
import string

# 759 -> Hash

knownhash = hash_str('nice')
print(knownhash)

available_string = string.ascii_lowercase

strs = []

for a in available_string:
    for b in available_string:
        for c in available_string:
            for d in available_string:
                s = f'{a}{b}{c}{d}'
                if hash_str(s) == knownhash:
                    strs.append(s)


print(strs)
print(len(strs))
