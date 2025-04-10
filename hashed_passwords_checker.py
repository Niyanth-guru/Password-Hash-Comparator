import hashlib
import time

# List of functions specific to hash algorithm for comparing purposes.
def compare_md5(digest):
    print("[+]Comparing the hash against known passwords......\n")
    time.sleep(1)
    with open("Passwords_dictionary.txt", 'r') as f:
        for word in f:
            word = word.strip()
            hashed = hashlib.md5(word.encode()).hexdigest()
            if hashed == digest:
                print(f"[+]Match found (MD5): {word}\n")
                time.sleep(1)
                return word
    print("[-]No match found using MD5.\n")
    time.sleep(1)
    return None

def compare_sha1(digest):
    print("[+]Comparing the hash against known passwords......\n")
    time.sleep(1)
    with open("Passwords_dictionary.txt", 'r') as f:
        for word in f:
            word = word.strip()
            hashed = hashlib.sha1(word.encode()).hexdigest()
            if hashed == digest:
                print(f"[+]Match found (SHA1): {word}\n")
                time.sleep(1)
                return word
    print("[-]No match found using SHA1.\n")
    time.sleep(1)
    return None

def compare_sha256(digest):
    print("[+]Comparing the hash against known passwords......\n")
    time.sleep(1)
    with open("Passwords_dictionary.txt", 'r') as f:
        for word in f:
            word = word.strip()
            hashed = hashlib.sha256(word.encode()).hexdigest()
            if hashed == digest:
                print(f"[+]Match found (SHA256): {word}\n")
                time.sleep(1)
                return word
    print("[-]No match found using SHA256.\n")
    time.sleep(1)
    return None

def compare_sha512(digest):
    print("[+]Comparing the hash against known passwords......\n")
    time.sleep(1)
    with open("Passwords_dictionary.txt", 'r') as f:
        for word in f:
            word = word.strip()
            hashed = hashlib.sha512(word.encode()).hexdigest()
            if hashed == digest:
                print(f"[+]Match found (SHA512): {word}\n")
                time.sleep(1)
                return word
    print("[-]No match found using SHA512.\n")
    time.sleep(1)
    return None

def compare_sha224(digest):
    print("[+]Comparing the hash against known passwords......\n")
    time.sleep(1)
    with open("Passwords_dictionary.txt", 'r') as f:
        for word in f:
            word = word.strip()
            hashed = hashlib.sha224(word.encode()).hexdigest()
            if hashed == digest:
                print(f"[+]Match found (SHA224): {word}\n")
                time.sleep(1)
                return word
    print("[-]No match found using SHA224.\n")
    time.sleep(1)
    return None

def compare_sha384(digest):
    print("[+]Comparing the hash against known passwords......\n")
    time.sleep(1)
    with open("Passwords_dictionary.txt", 'r') as f:
        for word in f:
            word = word.strip()
            hashed = hashlib.sha384(word.encode()).hexdigest()
            if hashed == digest:
                print(f"[+]Match found (SHA384): {word}\n")
                time.sleep(1)
                return word
    print("[-]No match found using SHA384.")
    time.sleep(1)
    return None

if __name__ == "__main__":
    # Getting the hashed password and hashing algorithm from the user.
    md =input("Enter the hash to match:")
    hash_algo = input("Enter the hash algorithm used(MD5/SHA variations):")
    print("[+]Analysing the input submitted\n")
    time.sleep(1)
    print("[+]Please wait.....\n")
    time.sleep(1)
    # Mapping of given input to call respective hash function
    algorithms ={"md5":compare_md5,"sha1":compare_sha1,"sha256":compare_sha256,"sha512":compare_sha512,"sha224":compare_sha224,"sha384":compare_sha384}
    # Calling the respective hash function that user gave
    if hash_algo in algorithms:
        algorithms[hash_algo](md)
    else:
        time.sleep(1)
        print("[+]Unsupported hash algorithm submitted.\n")
    time.sleep(1)
    print("[+]Program has ended....")