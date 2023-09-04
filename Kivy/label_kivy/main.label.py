import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.interactive import InteractiveLauncher

class TelaLabel(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Main_label(App):
    def build(self):
        return TelaLabel()

janela = Main_label()
janela.run()