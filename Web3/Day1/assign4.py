# Hash a file
import sys
import hashlib


def hashfile(file):

    # A arbitrary (but fixed) buffer size
    # 65536 = 65536 bytes = 64 kilobytes
    BUF_SIZE = 65536

    # Initializing the sha256() method
    sha256 = hashlib.sha256()

    # Opening the file provided as the first 
    # commandline argument
    with open("test.txt", 'rb') as f:
        while True:
            # reading data = BUF_SIZE from the 
            # file and saving it in a variable
            data = f.read(BUF_SIZE)

            # True if eof = 1
            if not data:
                break

            sha256.update(data)
    return sha256.hexdigest()


# Calling hashfile() function to obtain hash of the file 
# and saving the result in a variable
file_hash = hashfile(sys.argv[0])

print(f"Hash:{file_hash}")
