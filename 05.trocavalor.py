#Crie um algoritmo que armazene dois valores distintos (A=5 e B=10).
#Depois efetue a troca dos valores de forma que a variável A passe a possuir o valor da variável B e que a variável B passe a possuir o valor da variável A.
#Por fim, apresentar os valores trocados. (A=10 e B=5)
a=5
b=10
print("Os valores de A e B são respectivamente", a, "e", b)
auxiliar=a
a=b
b=auxiliar
print("Agora A= ", a, "e B= ", b)
