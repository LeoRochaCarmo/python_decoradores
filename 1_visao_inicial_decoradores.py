#%% 
# DECORADORES
# São funções que embrulham outras funções

# EXEMPLO -> Medidor de Tempo
from time import sleep
from time import time

def medidor_de_tempo(func):
    def aninhada(*args, **kwargs):
        t1 = time()
        resultado = func(*args, **kwargs)       
        t2 = time() - t1
        print(f'{func.__name__} demorou {t2} segundos')
        return resultado
    return aninhada

@medidor_de_tempo
def delay(secs):
    # Coloca o código pra dormir por 'secs'
    sleep(secs)
    return secs

print(delay(2))

#%%
# EXEMPLO -> Decorador de cache
from functools import cache

@medidor_de_tempo # segundo decorator a executar
@cache # primeiro decorator a executar
def delay(secs):
    # Coloca o código pra dormir por 'secs'
    sleep(secs)
    return secs

def print_func(*args):
    print(*args, sep='\n')

print_func(
    delay(3), delay(2), # guarda na mémoria os resultados 
    delay(3), delay(2), # reutiliza os resultados
)