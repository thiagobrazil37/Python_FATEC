from hashlib import sha256

user_padrao = "14514307be9ef4287877636f9a3397b7bb9dddfded42ee0449e8c83ac2f2a78a"
pass_padrao = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"

login_user = input("Digite seu usuário: ")
login_encode = login_user.encode("ascii")
pass_user =  str(input("Digite sua senha: ")).encode("ascii")

pass_user = sha256(pass_user).hexdigest()
login_check = sha256(login_encode).hexdigest()



if login_check == user_padrao and pass_user == pass_padrao:
    print(f"Bem vindo ao sistema, {login_user}!")
else:
    print(f"Caro {login_user}, verifique se seu login e/ou senha está(ão) preenchido(s) corretamente(s).")
    