# -*- coding: utf-8 -*-
import sys
sys.path.insert(1, '../model')
sys.path.insert(2, '../view')
sys.path.insert(3, '../controller')

from Matriz import Matriz
import Registro as registro
import rasp

print("- Sistema automatico para alimentação de matrizes suinas -")
print("1 - Cadastro de matrizes")
print("2 - Consulta de matrizes")
print("3 - Consulta de matriz")
print("4 - Registros de alimentação")
print("5 - Registro de alimentação por rfID de matriz")
print("6 - Iniciar alimentador")

opc = int(input("-> "))

if opc == 1:
    print("- Cadastro de matrizes -")
    matriz = Matriz(rasp.leitorRFID(), str(input('Insira a quantidade: ')))
    matriz.inserirMatriz()
elif opc == 2:
    print("- Consulta de matrizes -")
    matriz.consultarMatriz()
elif opc == 3:
    print("- Consulta de matriz -")
    matriz.consultarMatrizes()
elif opc == 4:
    print("- Registros de matrizes -")
    registro.consultarRegistros()
elif opc == 5:
    print("- Registros de matriz -")
    registro.consultarRegistro()
elif opc == 6:
    print("- Iniciando alimentador -")
    rasp.iniciarAlimentador()
else:
    print("Erro")