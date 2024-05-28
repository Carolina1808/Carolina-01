# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import random
#def adivinhe_o_numero():
 #   random.seed(25)
#    numero_aleatorio = random.randint(1, 100)
#    tentativas = 0
 #   acertou = False
 #   print("Adivinhe o número entre 1 e 100")

 #   while not acertou:
#     palpite = int(input("Digite seu palpite: "))
#     tentativas += 1
#     if palpite < numero_aleatorio:
   #      print("Muito baixo!")
 #    elif palpite > numero_aleatorio:
  #       print("Muito alto!")
  #   else:
   #      print(f"Você adivinhou em {tentativas} tentativas.")
 #        acertou = True
     
#adivinhe_o_numero()


import random

def lancamento_dado():
    resultado = random.randint(1, 6)
    return resultado

# Testando a função
resultado_lancamento = lancamento_dado()
print("O resultado do lançamento do dado é:", resultado_lancamento)
