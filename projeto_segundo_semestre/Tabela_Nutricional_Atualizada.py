from Carnes import Carnes
from Frutas import Frutas
from Graos import Graos
from Liquidos import Liquidos
from Verduras import Verduras

import os
import time

#CRIANDO OS ALIMENTOS
Frango = Carnes("Frango", 100, 159, 0, 32, 0, 50)
ArrozBranco = Graos("ArrozBranco", 100, 32, 7.03, 0.63, 0.40, 0.25)
FeijãoPreto = Graos("FeijãoPreto", 100, 77, 14, 4.5, 8.4, 1.9)
BatataDoce = Verduras("BatataDoce", 100, 53.90, 12.88, 0.42, 2.10)
Banana = Frutas("Banana", 100, 39.60, 10.32, 0.52, 0)
Maça = Frutas("Maça", 100, 67.60, 17.95, 0.34, 1.30)

#LISTA PARA ARMAZENAR OS NOMES DOS ALIMENTOS
listaNomesAlimentos = []
listaNomesAlimentos.append(Frango._nome)
listaNomesAlimentos.append(ArrozBranco._nome)
listaNomesAlimentos.append(FeijãoPreto._nome)
listaNomesAlimentos.append(BatataDoce._nome)
listaNomesAlimentos.append(Banana._nome)
listaNomesAlimentos.append(Maça._nome)

