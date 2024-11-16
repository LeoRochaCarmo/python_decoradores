from time import time

def medidor_de_tempo(func):
    def aninhada(*args, **kwargs):
        t1 = time()
        resultado = func(*args, **kwargs)       
        t2 = time() - t1
        print(f'{func.__name__} demorou {t2} segundos')
        return resultado
    return aninhada