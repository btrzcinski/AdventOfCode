def has_increasing_trigram(password):
    trigrams = [password[i:i+3].encode("utf-8") for i in range(len(password)-2)]
    valid_trigrams = [t for t in trigrams if t[2] == t[1] + 1 and t[1] == t[0] + 1]
    return len(valid_trigrams) > 0

def has_repeated_letter_pairs(password, num_pairs=2):
    pairs = [password[i:i+2] for i in range(len(password)-1)]
    repeated_pairs = len(set([p for p in pairs if p[0] == p[1]]))
    return repeated_pairs >= num_pairs

def is_valid_password(password):
    if not has_increasing_trigram(password): return False
    if 'i' in password: return False
    if 'o' in password: return False
    if 'l' in password: return False
    if not has_repeated_letter_pairs(password, 2): return False
    return True

def increment_password(password):
    letter = -1
    password = list(password)
    while letter >= -len(password):
        if password[letter] == 'z':
            password[letter] = 'a'
            letter -= 1
        else:
            inc = 1
            if password[letter] in ('h', 'n', 'k'): inc = 2
            password[letter] = chr(password[letter].encode("utf-8")[0] + inc)
            break
    return "".join(password)

def next_password(password):
    new_password = password
    while new_password == password or not is_valid_password(new_password):
        new_password = increment_password(new_password)
    print (password, "=>", new_password)
    return new_password

def main():
    password = "hxbxwxba"
    password2 = next_password(password)
    print("Next password: %s => %s" % (password, password2))
    password3 = next_password(password2)
    print("Next password: %s => %s" % (password2, password3))

if __name__ == "__main__":
    main()
