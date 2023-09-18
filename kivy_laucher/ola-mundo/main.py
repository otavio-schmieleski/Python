from kivy.lang import Builder
from kivymd.app import MDApp
#Kivy==2.2.1

kv = '''
MDScreen:
    MDRaisedButton:
        text: "botao"
        pos_hint: {"center_x": .5, "center_y": .5}
'''

class OlaMundo(MDApp):
    def build(self):
        return Builder.load_string(kv)


OlaMundo().run()



    