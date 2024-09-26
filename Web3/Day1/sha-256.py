# A Cryptographic hash function is a function that takes in input data and produces 
# a statistically unique output, which is unique to that particular set of data. 
# The hash is a fixed-length byte stream used to ensure the integrity of the data.

import hashlib

# A string that has been stored as a byte stream
string = b"hivemet"

# Initializing the sha256() method
sha256 = hashlib.sha256()

# Passing the byte stream as an argument
sha256.update(string)
# sha256.update(b"aws" + string)

# hexdigest() hashes the data, and returns the output in hexadecimal format

string_hash = sha256.hexdigest()

print(f"Hash:{string_hash}")

# Hash:df49b2a73a7fae138eb2b7bb3324279c8a7c4bda13ddd2c4a35f2dd53849cc84