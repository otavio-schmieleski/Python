import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

# aqui vai setar a cor de fundo da janela como branca
Window.clearcolor = [1,1,1,1]

class TelaCores(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_press_bt(self):
        # vai tira o widget da tela 2
        janela.root_window.remove_widget(janela.root)

        # vai adicionar o novo widget da tela 1 e executar
        janela.root_window.add_widget(TelaCores_de_Fundo())

class TelaCores_de_Fundo(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Sistema_de_cor(App):
    def build(self):
        return TelaCores()

janela = Sistema_de_cor()
janela.run()