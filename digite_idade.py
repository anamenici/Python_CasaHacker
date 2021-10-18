while True:
    idade = int(input("Digite a sua idade: "))
    if idade >= 16:
        print("Deu certo")
        break
    else:
        print(f" Você digitou {idade}, esse valor não vale")
        print("Errado, digite de novo.")

print(f"A idade digitada foi de {idade}")
print("Saiu do loop")
