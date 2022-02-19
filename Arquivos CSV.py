from ast import Import
import csv


import csv
with open('caso.csv', 'r') as arquivo_csv:
    leitor = csv.reader()
    linhas = linhas.split('\n')
    for linha in linhas:
     linhas = linhas.split(',')
print(linha)

with open('users.csv', 'w', newline='') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome', 'e-mail', 'genero'])
    escritor.writerow(['Luan', 'Oliveira', 'luangreen@gmail.com', 'Masculino'])





