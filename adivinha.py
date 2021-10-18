numero_secreto = 42

chance = 5
while chance > 0:
    tentativa = int(input("Digite um número qualquer para adivinhar o meu número secreto: "))
    chance -= 1
    if tentativa == numero_secreto:
        print("Você acertou!")
        break
    elif tentativa > numero_secreto:
        print("Errou! O número secreto é menor...")
        print(f"Você ainda tem {chance} chance(s)")
    else:
        print("Errou! O número secreto é maior...")
        print(f"Você ainda tem {chance} chance(s)")
    

print("Fim de jogo!")
