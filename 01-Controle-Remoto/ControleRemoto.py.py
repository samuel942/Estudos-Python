from rich import print
from rich.panel import Panel
from rich.text import Text

class ControleRemoto:
    """
    Controle Remoto com botoes funcionais, liga/desliga, aumenta ou diminui volume e 5 canais:
    0 -> desligar 
    @ -> ligar
    + e - -> aumentar ou diminuir volume
    < e > -> passar ou voltar o canal
    """
    def __init__(self):
        self.energia = False
        self.canal_atual = 1
        self.volume_atual = 0

    def ligar(self):
        if self.energia == False:
            self.energia = True

    def desligar(self):
        if self.energia == True:
            self.energia = False

    def exibir(self):

        if self.energia == False:
            conteudo_desligada = Text.from_markup(':prohibited:[red] TV desligada[/]')
            conteudo_desligada.justify = 'center'

            self.tv = Panel(
                conteudo_desligada,
                title = '[ TV ]',
                width = 25
            )
            print('\n' * 20)
            print(self.tv)

        else: 
            max_volume = '[green]██[/]' * self.volume_atual
            min_volume = '[grey37]██[/]' * (5 - self.volume_atual)
            vol = max_volume + min_volume

            canais = [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ']
            indice = self.canal_atual - 1
            canais[indice] = f'[black on yellow] {self.canal_atual} [/]'
            lista_canais = ''.join(canais)

            conteudo_ligada = Text.from_markup(f'CANAL  = {lista_canais}\nVOLUME = {vol}')
            conteudo_ligada.justify = 'left'

            self.tv = Panel(
                conteudo_ligada,
                title = '[ TV ]',
                width = 40
            )
            print('\n' * 7)
            print(self.tv)

    def canal(self, escolha):

        if escolha == '>':
            self.pular_canal()
        elif escolha == '<':
            self.voltar_canal()

    def pular_canal(self):
        if not self.energia: return

        if self.canal_atual == 5:
            self.canal_atual = 1
        else: 
            self.canal_atual += 1

    def voltar_canal(self):
        if not self.energia: return

        if self.canal_atual == 1:
            self.canal_atual = 5
        else:
            self.canal_atual -= 1

    def alterar_volume(self, escolha):
        
        if escolha == '+':
            self.aumentar_volume()
        elif escolha == '-':
            self.diminuir_volume()
    
    def aumentar_volume(self):
         
         if not self.energia: return
         if self.volume_atual < 5:
            self.volume_atual += 1

    def diminuir_volume(self):
        
        if not self.energia: return
        if self.volume_atual > 0:
            self.volume_atual -= 1
    
    def op(self):

        while True:
            self.exibir()
            escolha = input(f'< CH{self.canal_atual} >   - VOL{self.volume_atual} +  ')

            match escolha:

                case '@':
                    self.ligar()
                
                case '0':
                    self.desligar()
                
                case '<':
                    self.voltar_canal()

                case '>':
                    self.pular_canal()

                case '-':
                    self.diminuir_volume()

                case '+':
                    self.aumentar_volume()
                    
controle = ControleRemoto()
controle.op()