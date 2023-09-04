import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.interactive import InteractiveLauncher

class TelaTextInput(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ti = input.ids.text_input
        ti.text

class input(App):
    def build(self):
        return TelaTextInput()

janela = input()
janela.run()