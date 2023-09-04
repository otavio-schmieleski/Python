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

    def __init__(self, **kwargs):
        super(Tela1,self).__init__(**kwargs)
        self.orientation = 'vertical'
        bt1 = Button(text = 'clique') # criado os botoes

        # aqui associa o bt1 com a funcao de clique
        bt1.on_press = self.on_press_bt

        self.add_widget(bt1) # colocando na tela
        self.add_widget(Button(text ='btn1'))
        self.add_widget(Button(text ='btn2'))

class Tela2(BoxLayout):

    def on_press_bt(self):
        # vai tira o widget da tela 2
        janela.root_window.remove_widget(janela.root)

        # vai adicionar o novo widget da tela 1 e executar
        janela.root_window.add_widget(Tela1())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        bt = Button(text = 'clique')
        # associa o clique do botao com a funcao
        bt.on_press = self.on_press_bt
        self.add_widget(bt)

class button(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bt = Button(text = 'btn_ press')
        janela.add_widget(self.bt)
        self.bt.bind(on_press = self.click)
        self.bt.bind(on_release = self.fim_click)

    def click(self,bt):
        bt.text = 'on_press'
    def fim_click(self,bt):
        bt.text = 'on_realese'
    
        
    


class KVvsPY(App): # chamando a class tela 1 
    def build(self):
        return Tela1()

# executando a tela
janela = KVvsPY()
janela.run()