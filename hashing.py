import hashlib


def hash_file(fn):
    hash = hashlib.sha1()
    with open(fn, "rb") as file:
        chunk = 0
        while chunk != b"":
            chunk = file.read(1024)
            hash.update(chunk)
    return hash.hexdigest()


text = hash_file("textfile.txt")
print("hash of file is:", text)
