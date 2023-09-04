import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# estanciei uma janela box layout
class Tela1(BoxLayout):

    # quando o botao clique for precionado
    def on_press_bt(self):
        # vai tira o widget da tela 1
        janela.root_window.remove_widget(janela.root)
 
        # vai adicionar o novo widget da tela 2 e executar
        janela.root_window.add_widget(Tela2())

class Tela2(BoxLayout):

    def on_press_bt(self):
        # vai tira o widget da tela 2
        janela.root_window.remove_widget(janela.root)

        # vai adicionar o novo widget da tela 1 e executar
        janela.root_window.add_widget(Tela1())


class KVvsPY2(App): # chamando a class tela 1 
    def build(self):
        return Tela1()

# a aplicacao kv tem que ser escrito tudo em minusculo exemplo kvvspy2 para ler automaticamente
# executando a tela
janela = KVvsPY2()
janela.run()