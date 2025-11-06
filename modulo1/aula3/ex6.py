palavra = input("Digite uma palavra")

tamanho = len(palavra)

ultima = tamanho - 1

while palavra[0] != "p" or palavra[ultima] != "s" or "i" not in palavra or "m" in palavra or "n" in palavra or tamanho <= 3:
    palavra = input("Digite uma palavra: ")

print("Acertou")
