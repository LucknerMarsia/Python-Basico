#Criando arquivo de texto

arquivo = open('arqtext.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula prática')
arquivo.close()

#Lendo arquivo de texto

leitura = open('arqtext.txt', 'r')
print(leitura.read())
leitura.close()