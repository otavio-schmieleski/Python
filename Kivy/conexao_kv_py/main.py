import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MinhaTela(BoxLayout):

    def click(self):
        # aqui conecta com o label do kv pelo id
        self.ids.lb1.text = 'ola'
        self.ids.lb2.text = 'ola denovo'


class Conexao_py_kivy(App):
    pass

janela = Conexao_py_kivy()
janela.run()