from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class RootWidget(FloatLayout):
    pass

class MedidaApp(App):

    def build(self):
        return RootWidget()

MedidaApp().run()

# valores percentuais
""" 
    1.0 = 100%
    0.01 = 1%
    post_hint = para posicao relativa (dicionario)
    post_hint : {'right',0.1} para posicao a direita
    top = posicao em relacao ao topo da tela
    center_x = relacao com o eixo x do centro do componente
    center_y = relacao com o eixo y do centro do componente
    size_hint_x = para colocar o tamanho do eixo x do componente
    size_hint_y = para colocar o tamanho do eixo y do componente

"""