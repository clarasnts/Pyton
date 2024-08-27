print ("Bem-vindo a calculadora de IMC!")
nome = input("Qual seu nome?: ")
print ("Olá", nome)
peso = float(input("Qual o seu peso?: "))
altura = float(input("Qual a sua altura?: "))

print ("Vamos calcular o seu IMC!")

imc = (peso / (altura * altura))

print (nome, "este é seu IMC:", imc)

if imc<18.5:
    print("Seu peso está abaixo do normal.")
elif imc<24.9:
    print("Seu peso está normal.")
elif imc<29.9:
    print("Você está acima do peso.")
elif imc<34.9:
    print("Seu caso é de obesidade nível I.")
elif imc<39.9:
    print("Seu caso é de obesidade nível II.")
else:
    print("Seu caso é de obesidade nível III.")