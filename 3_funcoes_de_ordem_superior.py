#%%
# FUNÇÕES DE ORDEM SUPERIOR

# São funções que recebem ou retornam outras funções.

# Exemplos de funções: sorted, reduce, filter, etc

def inverter_palavra(palavra):
    return palavra[::-1]

palavras = [
    'sair', 'cair', 'fingir',
    'vazar', 'ser', 'ter',
    'estar', 'nevar',
]

for palavra in palavras:
    print(inverter_palavra(palavra))

sorted(palavras, key=inverter_palavra)

#%%
# Exemplo com a função filter

# Filtrando pessoas com mais de 30 anos de idade
pessoas = [
    {"nome": "Ana", "idade": 28, "profissao": "Engenheira"},
    {"nome": "Carlos", "idade": 34, "profissao": "Professor"},
    {"nome": "Mariana", "idade": 25, "profissao": "Designer"},
    {"nome": "Roberto", "idade": 40, "profissao": "Médico"},
    {"nome": "Lucas", "idade": 30, "profissao": "Desenvolvedor"},
    {"nome": "Fernanda", "idade": 27, "profissao": "Advogada"}
]

pessoas_mais_30 = list(filter(
    lambda pessoa: pessoa['idade'] > 30, 
    pessoas
))

print(*pessoas_mais_30, sep='\n')

#%%
# Exemplo de retorno de função: HOF PERSONALIZADA
def aplica_duas_vezes(func, valor):
    return func(func(valor))

def soma_1(x):
    return x + 1

aplica_duas_vezes(soma_1, 1)

#%%
# Exemplos de função que retorna outra função: partial
from functools import partial

def soma(x, y):
    return x + y

soma_3 = partial(soma,3)
soma_5 = partial(soma,5)

print(soma_3(3))
print(soma_5(3))

#%%
# HOF PERSONALIZADA -> usando a função map
l1 = [2, 4, 6]
l2 = [2, 4, 6]

def zip_with(func, *args):
    return list(map(func, *args))

print(zip_with(soma, l1, l2))

#%%
# HOF PERSONALIZADA -> EXEMPLO INSANO

def zip_with_2(func):
    return partial(map, func)

zip_soma = zip_with_2(soma)

print(list(zip_soma(l1, l2)))


