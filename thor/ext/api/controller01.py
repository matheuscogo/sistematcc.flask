import sys
sys.path.insert(1, '../model')
sys.path.insert(2, '../view')
sys.path.insert(3, '../controller')

import Matriz
import Registro
import View

class Controller:

    def start(self):
        opcao = self.view.start(self)

        while opcao != 0:
            self.opcao(opcao)
            opcao = self.view.menu()

        self.view.finalizar()


    def opcao(self, opcao):
        if opcao == 1:
            print(self.matriz.inserir())
        elif opcao == 2:
            print(self.matriz.consultar())
        elif opcao == 3:
            self.matriz.consultarPorRFID()
        elif opcao == 4:
            self.registro.consultar()
        elif opcao == 5:
            print(self.registro.consultarPorRFID())
        elif opcao == 6:
            self.registro.iniciar()

    def __init__(self):
        self.matriz = Matrizes
        self.registro = Registros.Registro()
        self.view = View.View

    def main(self):
        self.view.start()

if __name__ == '__main__':
    main = Controller()
    main.start()
