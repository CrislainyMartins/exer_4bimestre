#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letraescrever: F - Feminino, M - Masculino,Sexo Inválido.
letra=input('digite seu gênero')
if letra=="f" or "F":
    print('gênero feminino')
elif letra=="m" or "M":
    print('gênero masculino')
else:
    print('sexo invalido')


