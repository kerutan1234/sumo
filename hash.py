def hash_generator(filename):
    import hashlib
    with open(filename,'rb') as f:
        checksum = hashlib.sha256(f.read()).hexdigest()
    return(checksum)

if __name__ == '__main__':
    print(hash_generator("a.jpg"))
    pass