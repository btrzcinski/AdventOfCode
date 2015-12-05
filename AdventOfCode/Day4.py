import hashlib

def lowest_salt_with_leading_zeroes(secret_key, num_zeroes=5):
    leading_zeroes = "0" * num_zeroes
    salt = 0
    md5_hash = "abcdef"
    encoded_secret_key = secret_key.encode('utf-8')
    while not md5_hash.startswith(leading_zeroes):
        salt += 1
        m = hashlib.md5()
        m.update(encoded_secret_key)
        m.update(str(salt).encode('utf-8'))
        md5_hash = m.hexdigest()
    return salt

if __name__ == "__main__":
    print("5 zeroes: %d" % (lowest_salt_with_leading_zeroes("yzbqklnj"),))
    print("6 zeroes: %d" % (lowest_salt_with_leading_zeroes("yzbqklnj", 6),))
