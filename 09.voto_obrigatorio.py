nome=str(input("Qual seu nome?: "))
print("Olá", nome,"!")
idade= int(input("Quantos anos você tem?: "))
print("Você tem", idade, "anos!")

if idade>=18 and idade<=65:
    print("Seu voto é obrigatorio!")

elif idade<=16 or idade<=65:
    print("Você não tem direito a voto!")
else:
    print("Seu voto não é obrigatorio")