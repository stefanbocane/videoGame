import kivy
# Requires 
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class StartScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
    
        self.button = Button(text="Login", size_hint=(.1, .1), pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.button)
        if 


        

    #def on_release(self):
        #self.source = 'atlas://data/images/defaulttheme/checkbox_off'


     



class MyApp(App):
    def build(self):
        #return StartScreen()
        return StartScreen()



if __name__ == '__main__':

    MyApp().run()