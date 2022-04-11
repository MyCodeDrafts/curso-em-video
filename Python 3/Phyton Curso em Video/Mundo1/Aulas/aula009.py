# FATIAMENTO
frase = 'Curso em video Python'
print(frase[9::3])
print(frase[9])
print(frase[9:21:2])
print(frase[1:13])

# ANÁLISE
# len -> Mostra o comprimento da string
frase = 'Curso em Video Python'
len(frase)
print(len(frase))
# count -> Mostra quantas vezes aparece a letra na frase, nesse caso a letra o
frase = 'Curso em Vídeo Python'
print(frase.count('o'))
print(frase.count('o', 0, 13))  # Faz a contagem de o do zero ao 12
# find -> Mostra em que momento da string o deo começou
frase = 'Curso em Vídeo Python'
print(frase.find('deo'))
# in ... -> Mostra se tem a palavra na string
frase = 'Curso em Vídeo Python'
print('Curso' in frase)

# TRANSFORMAÇÃO
# replace -> Faz a substituição da palavra escolhida
frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))
# upper() -> Muda as letras que são minúsculas para maiúsculas
frase = 'Curso em Vídeo Python'
print(frase.upper())
# lower() -> Muda as letras que são maiúsculas para minúsculas
frase = 'Curso em Vídeo Python'
print(frase.lower())
# capitalize() -> Deixa o primeiro caractere em maiúsculo
frase = 'Curso em Vídeo Python'
print(frase.capitalize())
# title() -> Deixa as primeiras letras em maiúsculas
frase = 'Curso em Vídeo Python'
print(frase.title())
# strip() -> Tira os espaços inúteis da frase
frase = '   Aprenda Python  '
print(frase.strip())
# rstrip() -> (right) Remove os da direita
frase = '   Aprenda Python  '
print(frase.rstrip())
print(frase.lstrip())  # lstrip() -> (left) Remove os espaços da esquerda

# DIVISÃO
# split() -> Cria divisão ondem tem espaços e cria uma lista
frase = 'Curso em Vídeo Python'
print(frase.split())
print('-'.join(frase))



