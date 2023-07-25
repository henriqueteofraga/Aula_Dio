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