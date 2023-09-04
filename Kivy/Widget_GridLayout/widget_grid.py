import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.interactive import InteractiveLauncher

class TelaGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Widget_grid(App):
    def build(self):
        return TelaGridLayout()

janela = Widget_grid()
janela.run()