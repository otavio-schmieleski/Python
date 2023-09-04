import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.interactive import InteractiveLauncher

class TelaFloatLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Widgets_float(App):
    def build(self):
        return TelaFloatLayout()

janela = Widgets_float()
janela.run()