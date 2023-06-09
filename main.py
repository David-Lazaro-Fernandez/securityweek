import hashlib
# with open("apache_access.bib", "r") as file:
#     for line in file: 
#         elements = line.split(" ")
#         transaction = {
#             'ip' : elements[0],
#             'timestamp' : "".join([elements[3].strip("[]"),elements[4].strip("[]")]),
#             'kind_of_petition' : elements[5],
#             'route' : elements[6],
#             'version' : elements[7].strip('"'),
#             'status' : elements[8],
#             'completed_time': elements[9].strip('\n')
#         }
        
"""    
with open("numbers.txt","a") as file: 
   for number in range(16,21):
        file.write(str(number) + "\n")


secret_message = "Hey this is a secret!"
encoded_message = secret_message.encode()
secret_hash= hashlib.sha256(encoded_message)

print(secret_hash.hexdigest())
"""

def calculate_file_hash(file_path, algorithm='sha256'):
    """Calculate the hash value of a file using the specified algorithm."""
    hash_object = hashlib.new(algorithm)
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(4096)  # Read the file in chunks
            if not data:
                break
            hash_object.update(data)
    return hash_object.hexdigest()

def compare_files(file1_path, file2_path):
    """Compare two files by comparing their hash values."""
    file1_hash = calculate_file_hash(file1_path)
    file2_hash = calculate_file_hash(file2_path)
    
    if file1_hash == file2_hash:
        print("Files are identical.")
        print(file1_hash)
        print(file2_hash) 
    else:
        print("Files have changed.")
        print(file1_hash)
        print(file2_hash) 
file1 = 'hacker.txt'
file2 = 'hack_text.txt'

compare_files(file1, file2)
