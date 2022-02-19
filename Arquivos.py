arquivo = open('fase2.txt', 'r')
texto = arquivo.read()
print(texto)
arquivo.close()

arquivo = open('fase2.txt', 'r')
linha = arquivo.readline()
while linha != '':
    print(linha, end='')
    linha = arquivo.readline()
arquivo.close()

arquivo = open('fase2.txt', 'r')
for linha in arquivo:
    print(linha, end='')
    arquivo.close()

with open('fase2.text', 'r') as arquivo:
    text = arquivo.read()
    print(texto)

#arquivo do 0

with open('fase2.txt', 'w', ) as arquivo:
    arquivo.write(' Essa é uma linha que eu escrevi usando python\n')

with open('fase2.txt', 'r') as arquivo:
    print(arquivo.read(), end='')


with open('fase2.txt', 'a', ) as arquivo:
    arquivo.write(' Essa é uma linha que eu escrevi usando python\n')

#'r' read leitura
#'w' write - escrita no documento

