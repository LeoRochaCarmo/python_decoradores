#%% 
# DECORADORES
# São funções que embrulham outras funções

# EXEMPLO -> Medidor de Tempo
from time import sleep
from time import time

def medidor_de_tempo(func):
    def aninhada(*args, **kargs):
        t1 = time()
        func(*args, **kargs)
        t2 = time() - t1
        return f'{func.__name__} demorou {t2} segundos'
    return aninhada

@medidor_de_tempo
def delay(secs):
    sleep(secs)
    return secs

print(delay(2))