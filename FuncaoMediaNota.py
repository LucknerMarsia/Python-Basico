def lerNotas():
    n=float(input('Digite uma nota para o aluno(a): '))
    return n

def resultados(n1, n2):
    media = (n1 + n2)/2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Media: ", media, "Resultado: ", end="")
    if media >= 7.0:
        print("Aprovado")
    else:
        print("Reprovado")


a = lerNotas()
b = lerNotas()
resultados(a, b)