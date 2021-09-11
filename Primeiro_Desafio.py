"""
## OBS - Não altere a declaração da lista!
## Adicione o aluno na lista students com uma linha de código nova,
## utilizando uma função.

"""

studentes = ['Luiza', 'Amanda', 'Souza', 'Gustavo']

studentes.append('ivanesia')

print(studentes)

# Ops! A Luiza saiu do projeto. Remova a Luiza da lista.

studentes.remove('Luiza')

print(studentes)

"""
# Quantos alunos estão na lista? (consulte a quantidade usando a função 
# "len" dentro do print).

"""

print(len(studentes))

# No print faça uma operação para verificar se a "Bruno" está na lista students.
x = 'bruno'
if 'bruno' in studentes:
    print('Bruno está na lista')
else:
    print('Ele não está na lista')

# No print imprima a lista students em ordem reversa (reverse).

studentes.reverse()

print(studentes)

# Atribua à variável answer o valor da variável (option_a ou option_b)

print("De onde vem o print(option_a) e o len(option_b)?")
option_a = "Da Python Standard library"
option_b = "Do além"






