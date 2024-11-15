#Calculadora com escolha do usuário utilizando funções#
def exibirMenu():
    print(" ")
    print("######## MENU DA CALCULADORA #########")
    print("*****CATÁLOGO:*****")
    print("1. soma")
    print("2. subtração")
    print("3. multiplicação")
    print("4. divisão")
    print("5. Resto da divisão")
    print("6. Potencia")
    print("7. sair")

    opcao = int(input("Escolha sua opção: "))
    return opcao

opcao = 0

while True:
    opcao = exibirMenu()

    if opcao in [1,2,3,4,5,6]:
        valorA = float(input("Digite um valor: "))
        valorB = float(input("Digite um valor: "))

    if (opcao) in [1]:
        print(f"{valorA} + {valorB} = {valorA + valorB}")
    elif (opcao) in [2]:
        print(f"{valorA} - {valorB} = {valorA - valorB}")
    elif (opcao) in [3]:
        print(f"{valorA} x {valorB} = {valorA * valorB}")
    elif (opcao) in [4]:
        print(f"{valorA} : {valorB} = {valorA / valorB}")
    elif (opcao) in [5]:
        print(f" O resto da divisão de {valorA} por {valorB} é igual a {valorA % valorB}")
    elif (opcao) in [6]:
        print(f"{valorA} elevado a {valorB} = {valorA ** valorB}")
    elif (opcao) in [7]:
        print("Finalizando...")
        break

    else:
        print("Essa opção não é permitida, tente outra!")