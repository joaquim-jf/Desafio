import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

lista = ['Escolher uma música e cantar até o final  ',
         'Fazer um elogio ',
         'Fazer o máximo de flexões em 1 minuto',
         'Dar uma volta no campo de areia',
         'Mastigar um alho cru',
         'Chupar 1 limão ',
         'Segurar um cubo de gelo até ele derreter completamente',
         'Fazer uma pose de yoga e ficar parado nela por 10 segundos',
         'Fazer uma imitação de um famoso ou de alguém que está na festa',
         'mostrar como você faria para chegar em um crush',
         'Dar um beijo em uma fruta como se estivesse beijando alguém de língua',
         'Dançar na boquinha da garrafa',
         'Dançar na boquinha da garrafa',
         'Dançar na boquinha da garrafa',
         'Fazer uma performance de dança',
         'Ligar para um número desconhecido e peça uma pizza',
         'perna só por dois minutos', 'Fazer o 4 com as pernas',
         'Virar um copo de cerveja em uma golada só',
         'Preparar um drink', 'Um selinho em alguém ',
         'Um selinho na festa toda',
         'Um selinho na festa toda',
         'Um selinho na festa toda',
         'Simular sua posição sexual preferida',
         'Fazer uma dança sensual',
         'Simular sexo oral com uma fruta',
         'fazer uma massagem',
         'Beber uma dose na parte do corpo de outra pessoa',
         'Passar a língua pelo pescoço de alguém ',
         'Maquiar-se como um palhaço',
         'Quebrar o ovo com a boca',
         'Dançar um brega-funk ',
         'Enrolar a cabeça com papel higiênico e fica assim',
         'Fazer agachamentos por 1 minuto',
         'Em apenas 20 segundos pinte todas as unhas da mão',
         'Coloque um cubo de gelo dentro das calças por 1 minuto',
         'Lamba sua axila direta',
         'Coloque a cueca/calcinha por cima da roupa ',
         'Recite a tabuada do 2',
         'Cheire a axila de alguém',
         'Faça a dança do ventre',
         'Dê a volta em torno da mesa pulando num pé só',
         'Mie como um gato.',
         'Recite a tabuada do 9',
         'Recite o ABC de trás para frente',
         'Leve um tapa na cara de uma pessoa de sua escolha',
         'fazer um lap dance',
         'Faça uma rodada de “Transa, casa ou mata?” entre as pessoas da festa ',
         'Aperte as nádegas da pessoa à sua direita'
         ]

elemento = random.choice(lista)

class Test(App):
        def build(self):
            # returns a window object with all it's widgets
            self.window = GridLayout()
            self.window.cols = 1
            self.window.size_hint = (0.6, 0.7)
            self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

            # image widget
            self.window.add_widget(Image(source="Desafio.png"))

            # label widget
            self.greeting = Label(
                text="BOA SORTE ",
                font_size=18,
                color='#993399'
            )
            self.window.add_widget(self.greeting)

            # text input widget


            # button widget
            self.button = Button(
                text="JOGAR",
                size_hint=(1, 0.5),
                bold=True,
                background_color='#993399',
                # remove darker overlay of background colour
                # background_normal = ""
            )
            self.button.bind(on_press=self.callback)
            self.window.add_widget(self.button)

            return self.window

        def callback(self, instance):
            # change label text to "Hello + user name!"
            self.greeting.text = str(random.choice(lista))

    #def incrementar(self,button):
        #self.label.text = str(random.choice(lista))


# run Say Hello App Calss
if __name__ == "__main__":
    Test().run()