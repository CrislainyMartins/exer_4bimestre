#Faça um Programa que leia três números e mostre o maior deles.
n1=float(input('digite um numero '))
n2=float(input('digite um numero '))
n3=float(input('digite um numero '))
if n1>n2>n3 or n1>n3>n2:
    print('O maior número é: ', n1)
elif n2>n3>n1 or n2>n1>n3:
    print('O maior número é: ', n2)
elif n3>n2>n1 or n3>n1>n2:
    print('O maior número é ', n3)
