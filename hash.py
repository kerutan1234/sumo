def hash_generator(filename):
    import hashlib
    with open(filename,'rb') as f:
        checksum = hashlib.sha256(f.read()).hexdigest()
    print(checksum)
    return(checksum)

if __name__ == '__main__':
    pass