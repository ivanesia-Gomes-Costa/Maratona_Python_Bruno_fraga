#-----------------funcões-----------------
def welcome(name):
    msg = 'Ola ' + name.title()
    print(msg)


welcome('ivanesia gomes costa')
welcome('lucas alberto de souza')

#criando uma função de soma
"""
No exemplo da função abaixo, solicita dois valores, porém se o usuário informar somente um valor, a função ira apresentar
um erro. Para solucionar bastar desclara a variavel como sendo 0.
"""
def soma(n1=0, n2=0):
    calculo = n1 + n2
    print(calculo)

#criando uma função de subtração
def subtracao(s1, s2):
    calculo_sub = (s1 - s2)
    print(calculo_sub)

soma (15, 15)

subtracao (15, 15)


valor = int(input('Digite o valor de n1:  '))
segundo_valor = int(input('Digite o segundo valor: '))

soma(valor, segundo_valor)