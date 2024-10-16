print("CÍRCULO TRIGONOMETRICO")
print("CALCULANDO A TANGENTE")

import math

angulo = float(input( "digite o valor de um ângulo que deseja calcular:" ))

tangente = math.tan(math.radians(angulo))
print(" A tangente de {:.0f} graus é : {:.1f} graus" .format(angulo,tangente))

