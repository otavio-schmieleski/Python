import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.interactive import InteractiveLauncher

class TelaBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Widgets_box(App):
    def build(self):
        return TelaBoxLayout()

janela = Widgets_box()
janela.run()