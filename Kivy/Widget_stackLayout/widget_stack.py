import kivy
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.interactive import InteractiveLauncher

class TelaStackLayout(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Widget_stack(App):
    def build(self):
        return TelaStackLayout()

janela = Widget_stack()
janela.run()