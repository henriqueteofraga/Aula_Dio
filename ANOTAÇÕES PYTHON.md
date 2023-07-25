########################################################################################
PARTE 1
BASICO E CONTROLE DE FLUXO

"""string"""
#print("a")
"""int """
#print(1+5+6+9)
"""float"""
#print(1.5+6+9.0+80006.698)
"""blool"""
#print(True)
#print(False)

#conversão#
"""
nome = "henrique"
idade = "26"

print(float(idade))

nome ="26.9"
print(float(nome)) Resulta em erro
print(type(nome))
"""

#Funções entrada e saida#
"""
Função de entrada de dados: Input
Essa função pega e solicita uma entrada(vinda do teclado) e converte essa entrada para uma string(texto)

Função de saida de dados:Print
Essa função pega o dado parametrizado nos () e escreve em tela
#Exemplo#
nome = input("Digite seu nome: ")    \ Aqui o prompt vai escrever o que estiver entre "" e após isso, liberará para que o usuário digite algo
idade = input("Digite sua idade: ")  \ Aqui é a mesma coisa de cima

print(nome, idade)  \ Aqui está exibindo a variavel "nome" e "idade", que recebeu o dado escrito pelo comando inpu
print("teste", end="..." ) \ Aqui está exibindo os mesmos dados de antes, mas adicionando com o comando "end=" uma string a mais como parte final da mensagem
print(nome, idade, end="espaço\n") \ aqui a mesma coisa, mas o comando \n faz com que quebre a linha
print(f"Seu nome é {nome}, você tem {idade}anos", end=", Prazer em te conhecer.") \ aqui usei o comando de preenchimento de variavel dentro da string, não sendo necessário quebrar a string que está sendo escrita para adicionar o parametros
print("teste", "teste2" , sep="@") \ Aqui eu substitui o espaço que teria entre uma string e outra pelo @ usando o comando "sep=" 
"""
#Pratica de blocos de código/IF#

"""idade = int(input("Digite sua idade: "))
if idade < 18 :
    print("Você ainda não tem idade suficiente para poder tirar a carteira de motorista no Brasil")
else:
     print("Você está apto a tirar a carteira de motorista.")
"""
#saldo = 0

"""def deposito():
    valor_deposito = float(input("Digite quanto gostaria de depositar: "))
    saldo = 0
    saldo += valor_deposito
    return saldo """


"""opcao = 1
saldo = 0


def extrato():
     print(f"Seu saldo é R${saldo}")
def deposito():
     saldo = 0
     extrato()
     valor_deposito = float(input("Digite quanto gostaria de depositar: "))
     saldo += valor_deposito
def saque():
        print(saldo)
        valor_sacado = float(input("Digite o valor que deseja sacar: "))
        if saldo >= valor_sacado:
            saldo -= valor_sacado
            print(f"Você sacou{valor_sacado}, seu saldo em conta é {saldo}")   

while opcao != 0:
    print("Digite a opção desejada:")
    opcao = int(input(" [1]Extrato\n [2]Depositar \n [3]Sacar\n [0]Sair \n"))
    saldo = 0
    if opcao == 1:
        extrato()
    if opcao == 2:        
        deposito()
    if opcao == 3:
        saque()

#extrato()
#deposito()
#saque()"""

FIM PARTE 1
##########################################################################################

##########################################################################################
PARTE 2 - MANIPULAÇÃO DE STRING

nome = "   Henrique    "
'''print("Nome como eu defini")
print(nome)
print("Nome usando UPPER")
print(nome.upper())
print("Nome usando lower")
print(nome.lower())
print("Nome usando Title")
print(nome.title())
print("Nome usanod Center")
print(nome.center(20,"*"))
print("Nome usando join")
print(("-".join(nome)))
print("Nome usando strip")
print(nome.strip())
print("Nome usando lstrip")
print(nome.lstrip())
print("Nome usando rstrip")
print(nome.rstrip())
print("Nome usando UPPER e strip")
print(nome.upper().strip())'''
nome = ".".join(nome)
print(nome)

FIM PARTE 2

################################################################################################
 
 PARTE 3 - LISTA

 frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)
letras[1] = "i"
print(letras)
numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

frutas = ["maçã", "laranja", "uva", "pera"]

print(frutas[0])  # maçã
print(frutas[2])  # uva

frutas = ["maçã", "laranja", "uva", "pera"]

print(frutas[-1])  # pera
print(frutas[-3])  # laranja

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

"""
Como o nome já diz, serve pral impar uma lista
EXEMPLO ABAIXO ↓
"""

lista = [1, "Python", [40, 30, 20]]

print(lista)  # [1, "Python", [40, 30, 20]]

lista.clear()

print(lista)  # []

"""
n**2 if n > 6 else n for n in range(10) if n % 2 == 0
0
2
4
6
64

EXPLICAÇÃO
n começa no 0, 0 divido 2 sobra 0, se sobrar 0 ele guarda na memória o numero que o n era, ai o n aumenta em 1
1 divido por 2 não sobra 0 então ele não guarda na memória, sendo assim ele só vai guardar na memória numeros par
2 divido por 2 sobra zero, 4 divido por 2 sobra 0, 6 divido por 2 sobra 0, 8 divido por 2 sobre 0
como n é maior que 6 ele vai exponenciar
n só vai exponenciar ao quadrado(n**2) quando n for maior que 6.
como ele fez a exponenciação que era o que devia retornar como true no If, ele para a contagem
sendo assim a resposta é 
[0,2,4,6,64]
"""
# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

"""

SERVE PRA COPIAR UMA LISTA EM OUTRA NOVA, COM IDENTAÇÃO DIFERENTES NA MEMORIA SENDO POSSIVEL EDITAR AS LISTAS

"""

lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

""" 
SERVE PRA CONTAR QUANTAS VEZES O VALOR INFORMADO NO () APARECE NA LISTA

EXEMPLO ABAIXO ↓
"""

cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1

"""
SERVE PRA JUNTAR DUAS LISTA EM UMA
"""

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

""" 
SERVE PRA MOSTRAR EM QUAL INDICE APARECE A PRIMEIRA OCORRENCIA DO VALOR

EXEMPLO ABAIXO ↓
"""

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens)  # ["csharp", "java", "c", "js", "python"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens))  # 5

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

FIM PARTE 3 
##############################################################################################################

PARTE 4 - TUPLAS
frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
""" 
TUPLAS SÃO ARRAY'S/LISTAS IMUTAVEIS
"""

print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)

""" 

CONSEGUE-SE ACESSAR OS DADOS DELA IGUAL A UMA LISTA/ARRAY

"""

frutas = ("maçã", "laranja", "uva", "pera",)

print(frutas[0])  # maçã
print(frutas[2])  # uva

""" 
CONSEGUE-SE PERCORRER A TUPLA AO CONTRARIO IGUAL UM
"""

frutas = (
    "maçã",
    "laranja",
    "uva",
    "pera",
)

print(frutas[-1])  # pera
print(frutas[-3])  # laranja


""" 
A PARTE DE MATRIZ É IGUAL A UMA LISTA, PODENDO SER PERCORRIDA DO MESMO MODO
"""

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

""" 
CONSEGUE-SE FATIAR A TUPLA DO MESMO MODO QUE UMA LISTA

"""

tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])  # ("t", "h", "o", "n")
print(tupla[:2])  # ("p", "y")
print(tupla[1:3])  # ("y", "t")
print(tupla[0:3:2])  # ("p", "t")
print(tupla[::])  # ("p", "y", "t", "h", "o", "n")
print(tupla[::-1])  # ("n", "o", "h", "t", "y", "p")

""" 
CONSEGUE-SE ITERAR IGUAL UMA LISTA
"""

carros = (
    "gol",
    "celta",
    "palio",
)

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

""" 
A TUPLA POR SER IMUTALVE TEM MENOS METODOS BUILT-IN. 

COUNT É UM DELES, FUNCIONA DO MESMO MODO QUE UMA LISTA E SERVE PRA MOSTRAR QUANTAS VEZES O PARAMETRO 
DETERMINADO DENTRO DO () APARECE NA LISTAGEM/TUPLA
"""
cores = (
    "vermelho",
    "azul",
    "verde",
    "azul",
)

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1


""" 
A TUPLA POR SER IMUTALVE TEM MENOS METODOS BUILT-IN. 
INDEX É UM DELES, SERVE PRA MOSTRAR EM QUAL POSIÇÃO ESTÁ GUARDADO O VALOR DETERMINADO DENTRO DO ()
"""

linguagens = ("python", "js", "c", "java", "csharp",)

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

"""

A TUPLA POR SER IMUTALVE TEM MENOS METODOS BUILT-IN. 
LEN É UMA DELAS, VEM DA PALAVRA LENGHT QUE SERVE PRA MOSTRAR QUAL O TAMANHO TOTAL DA TUPLA

"""
linguagens = (
    "python",
    "js",
    "c",
    "java",
    "csharp",
)

print(len(linguagens))  # 5

FIM PARTE 4
###############################################################################################################

PARTE 5 - CONJUNTOS/SET
""" 
CONJUNTOS PODEM SER DEFINIDOS USANDO A PALAVRA SET

ELE PEGA OS VALORES REPETIDOS E IGNORA ELES, COMO NOS EXEMPLOS ABAIXOS:

TAMBÉM É POSSIVEL DECLARAR UM CONJUNTO USANDO {} EM VEZ DA PALAVRA SET, COMO NO EXEMPLO ABAIXO:

ELE NAO GARANTE ORGEM NAS HORA DE MOSTRAR NA TELA, PORTANTO  PODE ALTERAR A CADA VEZ QUE EXECUTAR O CÓDIGO
"""

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

nomes = {"Henrique", "Vitória", "Milena", "Fabiano", "Silvania"}
print(nomes) #{"Henrique", "Vitória", "Milena", "Fabiano", "Silvania"}

""" 
CONJUNTOS NÃO PODEM SER NAVEGADOS POR INDEXISAÇÃO IGUAL LISTAS/TUPLAS

PARA ISSO É NECESSÁRIO CONVERTER UM CONJUNTO EM UMA LISTA PARA PODER NAVEGAR POE ELA

EXEMPLO ABAIXO ↓
"""

numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])

"""  
AINDA ASSIM É POSSIVEL NAVEGAR POR CONJUNTOS UTILIZANDO O COMANDO FOR, FUNCIONA IGUAL UMA LISTA/TUPLA

EXEMPLO ABAIXO
"""

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

""" 
ESSE METODO SERVE PARA JUNTAR INFORMAÇÕES DE DOIS CONJUNTOS UTILIZANDO .union() EM UMA VARIAVEL


EXEMPLO ABAIXO
"""

conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print(resultado)

"""  
ESSE METODO FUNCIONA PARA JUNTAR INFORMAÇÕES QUE TEM EM COMUM ENTRE CONJUNTOS, UTILIZANDO O COMANDO .intersection()

EXEMPLO ABAIXO
"""

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)

"""  
ESSE METODO SERVE PARA MOSTRAR O QUE TEM DE DIFERENTE ENTRE UM CONJUNTO E OUTRO, UTILIZANDO O COMANDO ,difference()

EXEMPLO ABAIXO
"""

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado = conjunto_b.difference(conjunto_a)
print(resultado)

"""  
ESSE METODO SERVE PARA MOSTRAR O QUE APARECE EM UM CONJUNTO E NÃO NO OUTRO, EXIBINDO A DIFERENÇA ENTRE OS DOIS
CONJUNTOS 

por exemplo 
{1, 2, 3} - CONJUNTO A
{2, 3, 4} - CONJUNTO B
{1, 4} - RETORNO DO METODO MOSTRANDO QUE O 1 E O 4 SÃO OS UNICOS Q NAO SE REPETEM
"""
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a)
print(conjunto_b)

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)

"""  
ESSE METODO SERVE PRA MOSTRAR SE UM CONJUNTO É SUBCONJUNTO DE OUTRO

EXEMPLO:
conjunto_a = {1, 2, 3} 
conjunto_b = {4, 1, 2, 5, 6, 3}
O CONJUNTO_B CONTEM OS MESMO VALORES QUE O CONJUNTO_A, PORTANTO O CONJUNTO_A É UM SUBCONJUNTO DO CONJUNTO_B

UTILIZANDO O METODO .issubset() CASO O CONJUNTO QUE ESTIVER DENTRO DO PARENTESES TER OS VALORES QUE TEM TAMBÉM
NO CONJUNTO QUE ESTÁ CHAMANDO O METODO, ELE RETORNARÁ TRUE CASO NÃO FOR RETORNARÁ FALSE
"""

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)

"""  
ESSE METODO É O CONTRARIO DO METEODO ISSUBSET.

EM CASO DE DUVIDA, LER O ARQUIVO DO ISSUBSET

"""

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)

"""  
SERVE PRA MOSTRAR SE UM CONJUNTO É TOTALMENTE DIFERENTE DO OUTRO, SEM TER NENHUM VALOR IGUAL EM AMBOS

CASO NÃO TENHA NENHUM VALOR IGUAL EM AMBOS ELE RETORNARÁ TRUE
CASO TENHA ALGUM VALOR, INDEPENDENTE DE QUANTOS FOREM, RETORNARÁ FALSE

"""

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)

"""  
SERVE PARA ADICIONAR UM VALOR AO CONJUNTO, MAS APENAS CASO O VALOR NÃO EXISTA AINDA NO CONJUNTO
CASO JÁ EXISTA ELE IGNORA

"""

sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
print(sorteio)

sorteio.add(42)  # {1, 23, 25, 42}
print(sorteio)

sorteio.add(25)  # {1, 23, 25, 42}
print(sorteio)

""" 
COMO O NOME JÁ DIZ, SERVE PRA LIMPAR OS VALORES QUE TEM EM UM CONJUNTO
"""

sorteio = {1, 23}

print(sorteio)  # {1,23}

sorteio.clear()

print(sorteio)  # {}

""" 
SERVE PRA COPIAR UM CONJUNTO EM OUTRO
"""

sorteio = {1, 23, 45}

print(sorteio)  # {1, 23}

teste = sorteio.copy()

print(teste)  # {1, 23}

""" 
SERVE PRA TIRAR UM VALOR ESPECIFICADO NO ()

CASO O VALOR ESPECIFICADO TENHA NO CONJUNTO, ELE É REMOVIDO CASO NÃO TENHA O VALOR NO CONJUNTO O SISTEMA
APENAS IGNORA O COMANDO EM VEZ DE DAR ERRO
"""

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45)

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}

""" 
SERVE PRA REMOVER O PRIMEIRO VALOR DA ESQUERDA PRA DIREITA E NAO PODE TER PARAMETRO NO ()
"""

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.pop())  # 0
print(numeros.pop())  # 1
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}

""" 
QUASE IGUAL AO DISCARD, A UNICA DIFERENÇA É QUE CASO O VALOR NÃO EXISTA IRÁ DAR ERRO NO PROGRAMA
"""

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

""" 
SERVER PRA MOSTRAR O TAMANHO DO CONJUNTO, MAS NÃO LEVA EM CONTA VALORES DUPLICADO
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}  TEM 13 NUMERO, MAS SE USAR O LEN VAI MOSTRAR
APENAS 10 POIS IGNORA DUPLICADOS
"""

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(len(numeros))  # 10

""" 
SERVE PRA MOSTRAR SE O VALOR ESPECIFICADO ANTES DO IN EXISTE NO CONJUNTO INFORMADO, CASO EXISTA DA TRUE
CASO NÃO DA FALSE
"""

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros)  # True
print(10 in numeros)  # False
