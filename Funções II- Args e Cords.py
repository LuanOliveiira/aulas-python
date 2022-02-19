def calcula_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

def calcula_media(*args):
    print(args, type(arg))
calcula_media(10, 8, 9)

def calcula_media(*args):
    soma = sum(args)
    media = soma / len(args)
    return media
calcula_media(10, 8, 9)



