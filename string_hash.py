import string

def hash_str(string):
    const = 2
    ascii_nums = []

    for i, s in enumerate(string):
        hashcode = ord(s)*(const**i) + ord(s)**(const*i)
        # hashcode = ord(s)*(const**i)
        ascii_nums.append(hashcode)

    return sum(ascii_nums)

if __name__ == "__main__":
    print(hash_str("nice"))
