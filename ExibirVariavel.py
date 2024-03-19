'''codigo = 105
nome = 'José Santana'
salario  = 1650.00
ativo = True'''

'''Todo input simples é uma string, se inserir números é necessário converte-los conforme abaixo.'''

codigo = int(input("Digite o código do funcionário: "))
nome = input("Digite o nome do funcionário: ")
salario  = float(input("Informe o salário do funcionário: "))
ativo = True

print("Código: %d " % codigo)
print("Nome: %r" % nome)
print("Salário: %.2f " % salario)
print("Ativo %r" % ativo)