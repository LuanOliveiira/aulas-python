dados_cidade = {
    'nome' : 'São Paulo',
    'estado' : 'São Paulo',
    'area_km2' : 1512,
    'populacao_milhoes' : 12.18,
}

print(type(dados_cidade))

dados_cidade['pais'] = 'Brasil'
print(dados_cidade)
print(dados_cidade['nome'])

dados_cidade['area_km2'] = 1500

dados_cidade_2 = dados_cidade
dados_cidade_2['nome'] = 'Santos'

print(dados_cidade_2)

dados_cidade_3 = dados_cidade.copy()
dados_cidade_3['estado'] = 'Rio de Janeiro'
print(dados_cidade)

novos_dados = {
    'população_milhoes' : 15,
    'fundacao' : '25/01/1554'
}

dados_cidade.update(novos_dados)
print(dados_cidade)

print(dados_cidade.keys())
print('_ _ _ _')
print(dados_cidade.values())
print('_ _ _ _ ')
print(dados_cidade.items())



