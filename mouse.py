# Responsável pelo controle do mouse
from pynput.mouse import Listener, Button, Controller

mouse = Controller()

class MindMouse:
    def __init__(self,velocidade):
        self.velocidade=velocidade

    def direita(self):
        mouse.move(self.velocidade,0)

    def esquerda(self):
        mouse.move(-self.velocidade,0)

    def cima(self):
        mouse.move(0,self.velocidade)

    def baixo(self):
        mouse.move(0,-self.velocidade)

    def cliqueDireito(self):
        mouse.click(Button.right,1)

    def cliqueEsquerdo(self):
        mouse.click(Button.left,1)

    def cliqueEsquerdo2X(self):
        mouse.click(Button.left,2)

