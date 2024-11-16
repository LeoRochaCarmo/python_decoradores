#%%
# DECORADORES

# Uma closure pode ser um decorador se:
# * a função externa receber uma função
# * A função recebida é a variável livre
# * Retorna a função interna

# fábrica de funções
def decorador(func):
    def interna(*args):
        resultado = func(*args)
        return f'Sou uma closure e sua função retornou {resultado}'
    return interna

def soma(x, y):
    return x + y

decorada = decorador(soma)

decorada(1, 2)

#%%
# USANDO SYNTAX SUGAR PARA DECORADORES (@)
def decorador(func):
    def interna(*args):
        resultado = func(*args)
        return f'Sou uma closure e sua função retornou {resultado}'
    return interna

@decorador # açúcar sintático
def soma(x, y):
    return x + y

soma(1, 2)

#%%
# DECORADOR COM PARÂMETROS

# fábrica de decoradores
def cuida_do_parametro(param):
    def decorador(func):
        def closure(*args, **kwargs):
            print(param)
            print(func.__name__)
            return func(*args, **kwargs)
        return closure
    return decorador

@cuida_do_parametro(1)
def soma(x, y):
    return x + y

soma(1, 2)

#%%
# DECORADOR QUE EXECUTA A FUNÇÃO DE NOVO SE DER ERRADO

from time import sleep

def retry(erro, vezes, tempo):
    count = 0
    # erro, vezes e count são variáveis livres

    def intermediaria(func):

        def closure(*args, **kwargs):
            nonlocal count

            try:
                return func(*args, **kwargs)
            except erro as e:
                count += 1
                print(f'{func.__name__} error: {e} retry: {count}')
                if count < vezes:
                    sleep(tempo) # Tenta de novo depois de x segundos
                    return closure(*args, **kwargs)
                
        return closure
    return intermediaria

@retry(ZeroDivisionError, 5, 3)
def div(x, y):
    return x / y

div(3, 0)

#%%
# DECORADOR WRAPS

'''
O @wraps é um decorador da biblioteca functools em Python. Ele é usado para preservar metadados da função original que está sendo decorada. 
Quando uma função é decorada sem o uso de @wraps, as propriedades como __name__, __doc__, e __module__ da função original são substituídas pelas 
da função interna do decorador (neste caso, closure). Isso pode fazer com que a função decorada perca informações importantes, como seu nome e sua documentação.

Usando @wraps(func), a função decorada mantém esses metadados originais, o que é útil para garantir que a função decorada 
seja mais transparente em relação à função original.

No seu exemplo, a linha @wraps(func) em closure faz com que closure herde o nome, a documentação
 e outros atributos da função que está sendo decorada, preservando suas características originais.
'''

from functools import wraps
from medidor_de_tempo import medidor_de_tempo

# fábrica de decoradores
def cuida_do_parametro(param=None):
    def decorador(func):
        @wraps(func)
        @medidor_de_tempo
        def closure(*args, **kwargs):
            print(param)
            print(func.__name__)
            return func(*args, **kwargs)
        return closure
    return decorador

@cuida_do_parametro()
def soma(x, y):
    return x + y

soma(2,2)

#%%

from datetime import datetime

def debug(*, verbose=False, level=0):

    def intermediaria(func):

        def interna(*args, **kwargs):
            tstart = datetime.now()
            result = func(*args, **kwargs)
            t_final = datetime.now() - tstart
            if verbose:
                print(
                    f'Chamada {func.__name__}\n'
                    f'parâmetros posicionais: {args}\n'
                    f'parâmetros nomeados: {kwargs}\n'
                )
            if level > 0:
                print(f'Resultado: {result}')
            if level > 1:
                print(f'Tempo total: {t_final.total_seconds()}')
            return result
        return interna
    return intermediaria


@debug(verbose=True, level=2)
def soma(x, y):
    return x + y


soma(1, 1)

#%%

# REPOSITÓRIO COM LISTA DE DECORADORES

#https://github.com/lord63/awesome-python-decorator