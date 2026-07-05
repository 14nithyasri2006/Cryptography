import hashlib

text = input("Enter password: ")

hash_value = hashlib.sha256(text.encode()).hexdigest()

print("Hashed password:", hash_value)