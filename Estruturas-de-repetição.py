nome_cidades = ['São Paulo', 'Londres', 'Tóquio', 'Paris']
for nome in nome_cidades:
    print(nome)

contador = 0
nome_cidades = ['São Paulo', 'Londres', 'Tóqui', 'Paris']
while contador < len(nome_cidades):
    print(nome_cidades(contador))
    contador = contador + 1

nome_cidades = 'São Paulo', 'Londres', 'Tóquio', 'Paris'
for nome in nome_cidades:
    print(nome)

nome_cidades = { 
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'populacao_milhoes' : 12.2
}
for chave in cidade:
    print(f'{chave}: {cidade[chave]}')

for posicao in range(len(nome_cidades)):
    nome_cidades[posicao] = 'Rio de Janeiro'
print(nome_cidades)
