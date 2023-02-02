def hash_generator(filename):
    import hashlib
    with open(filename,'rb') as f:
        checksuma = hashlib.sha256(f.read()).hexdigest()
    print(checksuma)

if __name__ == '__main__':
    pass