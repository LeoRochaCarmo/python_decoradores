#%%
# FUNÇÕES ANINHADAS -> funções dentro de funções


# Esse exemplo não precisa ser feito assim. É apenas exemplo
def ola(nome):
    def func_interna(nome):
        if nome.lower() == 'marilene':
            print(f'Olá {nome}. A noite, tainha, vinho e muito...')
        else:
            print(f'Olá {nome}, boas vindas.')
    func_interna(nome)

ola('Marilene')
ola('Theo')

#%%
# FORMA BRUTA SEM FUNÇÃO ANINHADA

from unicodedata import normalize

palavras = ['Érico', 'Sabiá', 'João']

def normaliza(*palavras):
    saida = []

    for palavra in palavras:
        normalizado = normalize('NFKD', palavra)
        normalizada = normalizado.encode('ASCII', 'ignore').decode('ASCII')
        saida.append(normalizada)

    return saida

normaliza(*palavras)

#%%
# FORMA COM FUNÇÃO ANINHADA

def normaliza2(*palavras):
    def ajudante(palavra):
        normalizado = normalize('NFKD', palavra)
        return normalizado.encode('ASCII', 'ignore').decode('ASCII')
    
    return [ajudante(palavra) for palavra in palavras]

normaliza2(*palavras)

#%%
# CLOSURES -> funções que encapsulam uma função (interna) e a retornam.

def soma_x(val_externo):
    def interna(val_interno):
        return val_externo + val_interno
    return interna

soma_1 = soma_x(1) # Criação de partial
soma_10 = soma_x(10) # Criação de partial

print(soma_1(10))
print(soma_10(1))


#%%
# ESCOPO DE VARIÁVEIS (GLOBAL, LOCAL, NONLOCAL)

# global
def contador(start=0):
    count = start # count é uma variável livre

    def interna():
        #local
        nonlocal count # Declara que queremos usar a variável 'count' do escopo extern 
        count += 1
        return count
    
    return interna

c = contador()

print(c())
print(c())

#%%
# COMO SABER SE ALGO É UM CLOSURE E QUAIS VALORES E NOMES DAS VARIÁVEIS LIVRES

c.__closure__
c.__closure__[0].cell_contents # valor
c.__code__.co_freevars # nome da variável livre




