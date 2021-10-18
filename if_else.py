tempo = int(input("Digite o número de minutos "))

horas = tempo // 60
minutos = tempo % 60

if tempo < 60:
    print(f"São {minutos} minutos!")
else:
    print(f" São {horas} horas e {minutos} minutos!")
