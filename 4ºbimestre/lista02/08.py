#Faça um programa que pergunte o preço de três produtos e informe qual produto você
#deve comprar, sabendo que a decisão é sempre pelo mais barato.
p1=float(input('digite um numero '))
p2=float(input('digite um numero '))
p3=float(input('digite um numero '))
if p1<p2<p3 or p1<p3<p2:
    print('{} é o preço mais baixo'.format(p1))
elif p2<p1<p3 or p2<p3<p1:
    print('{} é o preço mais baixo'.format(p2))
elif p3<p1<p2 or p3<p2<p1:
    print('{} é o preço mais baixo'.format(p3))








