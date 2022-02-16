empresa = 'Google'
print(empresa)

empresa = "Google"
print(empresa)

empresa = "Let' s Code"
print(empresa)

frase = "O professor Pietro da Lets: \"Hoje a pizza é por minha conta\""
print(frase)

empresa = 'Google'
print(empresa[0])

print(empresa[:3])

nomes_cidades = "São Paulo, Belo Horizonte, Rio de Janeiro, Brasília"
nomes_cidades = nomes_cidades.split(', ')
print(nomes_cidades)

cabecalho = " MENU PRINCIAL "
print(cabecalho.strip())

nomes_cidade = 'rIo DE jaNeirO'
print(nomes_cidade.title())
print(nomes_cidade.capitalize())
print(nomes_cidade.lower())
print(nomes_cidade.upper())


nomes_cidade = input('Que cidade do Brasil é conhecida como cidade maravilhosa?')
nomes_cidade = nomes_cidade.strip()
while nomes_cidade.lower() != 'rio de janeiro' :
    print('Tenta de novo, vai')
    nomes_cidade = input('Que cidade do Brasil é conhecida como cidade maravilhosa')
    print('Booa, campeão!')

mensagem = 'Você viu o que o Peitro disse na sala ontem?'
fui_citado = 'Pietro' in mensagem
print(fui_citado)



