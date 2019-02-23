# Responsável pela conexão com o MindWave
from NeuroPy import NeuroPy

# Responsável pelo controle do Mouse
from mouse import MindMouse

# Responsável pela detecção do Teclado
from pynput import keyboard

# CONFIGURAÇÃO INICIAL #
neuro = NeuroPy("COM6") #Inicializando o MindWave
neuro.start()
'''Exemplos de inicialização:
#windows: object1=NeuroPy("COM6",57600)
#linux: object1=NeuroPy("/dev/rfcomm0",57600)'''

print('Digite uma velocidade de 5 a 15 (5 mais lento e 15 mais rápido):')
velocidade = input() #Definindo a velocidado do mouse
mouseVirtual = MindMouse(int(velocidade)) #Iniciando objeto mouse

# CÓDIGO TEMPORARIO
'''
Objetivo:
    Enquanto não estou fazendo uso do equipamento MindWave, para fazer
    os testes de manuseio do mouse, estou usando teclas:
    u - Cima
    j - Baixo
    h - Esquerda
    k - Direita
    l - um mouse click direito
    o - um mouse click esquerdo
    p - dois mouse clicks esquerdo
'''

def on_press(key):
    if key.char == 'k':
        mouseVirtual.direita()
    if key.char == 'h':
        mouseVirtual.esquerda()
    if key.char == 'j':
        mouseVirtual.cima()
    if key.char == 'u':
        mouseVirtual.baixo()
    if key.char == 'l':
        mouseVirtual.cliqueDireito()
    if key.char == 'o':
        mouseVirtual.cliqueEsquerdo()
    if key.char == 'p':
        mouseVirtual.cliqueEsquerdo2X()

def on_release(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

''' Assim que o equipamento estiver em funcionamento, será feita a seleção
dos sinais mais fáceis de interpretar para que sejam usados
para mover o cursor. '''

