from hashlib import sha256

cpf = b"12345678910"
print(cpf)
cpf = sha256(cpf)
print(cpf.hexdigest())
