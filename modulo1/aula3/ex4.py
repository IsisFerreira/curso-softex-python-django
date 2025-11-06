usuario = input("Digite um login")
senha = input("Digite uma senha")

if "admin" in usuario and len(senha) >= 6:
    print("Login correto")
else:
    print("Usuario ou senha invalidos")
