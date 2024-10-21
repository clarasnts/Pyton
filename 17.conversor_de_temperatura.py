
#celsis para fahrenheit
def celcius_fahrenheit(c):
    return (c * 9/5) + 32

# celsius para kelvin
def celcius_kelvin(c):
    return c + 273.15

#fahrenheit para celsius
def fahrenheit_celsius(f):
   return (f - 32) * 5/9
 
#fahrenheit para kelvin
def fahrenheit_kelvin(f):
   return (f - 32) * 5/9 + 273.15

#kelvin para celsius 
def kelvin_celsius(k):
   return k - 273.15

#kelvin para fahrenheit
def kelvin_fahrenheit(k):
   return (k - 273.15) * 9/5 + 32

#FUNÇÃO PRINCIPAL
def conversor():
 print("conversor de temperaturas")
while True:
  print("\n Escolha a operação: ")
  print("1-celsis para fahrenheit")
  print("2-celsius para kelvin")
  print("3-fahrenheit para celsius")
  print("4-fahrenheit para kelvin")
  print("5-kelvin para celsius")
  print("6-kelvin para fahrenheit")
  print("7-sair")

  opção = int(input("Digite o número da operação desejada:"))

  if opção==0:
     print("Saindo...")
     break
  
  temperatura = float(input("Digite a  temperatura: "))
  if opção==1:
     resultado=celcius_fahrenheit(temperatura)
     print(f"{temperatura}° C é igual a {resultado}° f")
  elif opção==2:
     resultado= celcius_kelvin(temperatura)
     print(f"{temperatura}° C é igual a {resultado}° K")
  elif opção==3:
     resultado= fahrenheit_celsius(temperatura)
     print(f"{temperatura}° f é igual a {resultado}° c")
  elif opção==4:
     resultado= fahrenheit_kelvin(temperatura)
     print(f"{temperatura}° f é igual a {resultado}° K")
  elif opção==5:
     resultado= kelvin_celsius(temperatura)
     print(f"{temperatura}° K é igual a {resultado}° c")
  elif opção==6:
     resultado= kelvin_fahrenheit(temperatura)
     print(f"{temperatura}° K é igual a {resultado}° f")
  else:
     print("opção inválida")
     conversor()
