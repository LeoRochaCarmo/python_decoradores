#%%
# FUNÇÕES DE PRIMEIRA CLASSE

# funções que podem ser manipuladas como qualquer outra variável.

def soma(x, y):
    return x + y

sominha = soma
somao = soma

print(sominha(1,2))
print(somao(43, 54))

 #%% 
 # lista de funções

list_funcs = [sominha, somao]

list_funcs[0](9, 10) #sominha
list_funcs[1](9, 10) #somão

#%%
# Criando calculadora com funções dentro de dicionários
from functools import reduce

def soma(*args):
    return reduce(lambda x, y: x + y, args)

def sub(*args):
    return reduce(lambda x, y: x - y, args)

def mul(*args):
    return reduce(lambda x, y: x * y, args)

def div(*args):
    return reduce(lambda x, y: x / y, args)

def calculadora(op, *args):
    operacoes = {
        '+': soma,
        '-': sub,
        '*': mul,
        '/': div,
    }
    return operacoes[op](*args)

calculadora('+', 3, 3, 3)
#%%
