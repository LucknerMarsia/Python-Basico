idade = int(input("Digite sua idade: "))
nome = input("Digite seu nome: ")

if idade > 18:
    print(nome, "você é maior de idade!")
elif idade > 15:
    print(nome, "Você é menor e infanto juvenil!")
else:
    print(nome, "você é menor de idade!")