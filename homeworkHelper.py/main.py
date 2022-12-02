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
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition 
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
import csv
import pandas as pd



textinput = TextInput(text='Hello world')
# info = {'Username': username,
#         'Password': password,
#         'Email': email}

class LoginWindow(Screen):
    
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(LoginWindow, self).__init__(**kwargs)
        self.add_widget(Label(text='Username', size_hint=(.45, .1), pos_hint={'x': .05, 'y': .7}))
        self.username = TextInput(multiline=False, size_hint=(.45, .1), pos_hint={'x': .5, 'y': .7})
        self.add_widget(self.username)
        self.add_widget(Label(text='Password', size_hint=(.45, .1), pos_hint={'x': .05, 'y': .5}))
        self.password = TextInput(multiline=False, password=True, size_hint=(.45, .1), pos_hint={'x': .5, 'y': .5})
        self.add_widget(self.password)
        
        self.btn = Button(text='First time? Enter some info!', size_hint=(.4, .1), pos_hint={'center_x': .7, 'y': .03})
        self.add_widget(self.btn)
        self.btn.bind(on_press=self.cont)

        self.log= Button(text='Login', size_hint=(.4, .1), pos_hint={'center_x': .3, 'y': .03})
        self.add_widget(self.log)
        self.log.bind(on_press=self.validate)

    

    def cont(self, instance):
        sm.current='register'
        return sm

    def validate(self, instance):
    
        if self.username.text == username and self.password.text == password:
            print("login verified")
            
            valid = Popup(title='Verified', content=Label(text='Continue!'), 
            size_hint=(None, None), size=(400, 400))
            
            valid.open()
        elif self.username.text != username or self.password.text != password:
            invalid = Popup(title='Invalid', content=Label(text='Try again!'), 
            size_hint=(None, None), size=(400, 400))
            
            invalid.open()
        
        

            
        
        

class StartScreen(Screen, FloatLayout):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
    
        self.button = Button(text="Begin", size_hint=(.3, .3), pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.button)
        self.button.bind(on_press=self.callback)
       
    

        u = Label(text='College Roomate Finder!', font_size='40sp', pos_hint={'center_x': .5, 'center_y': .8}) 
        self.add_widget(u)

  

    def callback(self, instance):
        sm.current='login'
        return sm
       

users= pd.read_csv('data.csv')

 # class to accept user info and validate it
class loginWindow(Screen):
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)
    

        

class RegisterWindow(Screen):
    global username
    global password
    
    
    def __init__(self, **kwargs):
        super(RegisterWindow, self).__init__(**kwargs)
        self.add_widget(Label(text='Username', size_hint=(.45, .1), pos_hint={'x': .05, 'y': .7}))
        self.username = TextInput(multiline=False, size_hint=(.45, .1), pos_hint={'x': .5, 'y': .7})
        self.add_widget(self.username)
        self.add_widget(Label(text='Password', size_hint=(.45, .1), pos_hint={'x': .05, 'y': .5}))
        self.password = TextInput(multiline=False, password=True, size_hint=(.45, .1), pos_hint={'x': .5, 'y': .5})
        self.add_widget(self.password)
        self.add_widget(Label(text='E-mail', size_hint=(.45, .1), pos_hint={'x': .05, 'y': .3}))
        self.email = TextInput(multiline=False, size_hint=(.45, .1), pos_hint={'x': .5, 'y': .3})
        self.add_widget(self.email)
        self.btn = Button(text='Register', size_hint=(.9, .2), pos_hint={'center_x': .5, 'y': .03})
        self.add_widget(self.btn)
        self.btn.bind(on_press=self.submit)

#Create a function for the button to be called upon
    def submit(self, instance):

     
        
        global username
        global password
        global email

   

        username = self.username.text
        print("Username set to ", username)
        password = self.password.text
        email = self.email.text

      
        self.username.text = ''
        self.password.text = ''
        self.email.text = ''

        print(username, password, email)        
        sm.current='login'
        return sm

class InitialQuestion(Screen):
    def __init__(self, **kwargs):
        super(InitialQuestion, self).__init__(**kwargs)

        self.add_widget(Label(text='Answer the Questions, Find a Roomate!', size_hint=(.45, .1), pos_hint={'x': .05, 'y': .9}))

        self.add_widget(Label(text='What food do you like?', size_hint=(.45, .1), pos_hint={'x': .05, 'y': .7}))
        self.username = TextInput(multiline=False, size_hint=(.45, .1), pos_hint={'x': .5, 'y': .7})
        self.add_widget(self.username)
        self.add_widget(Label(text='How would you describe your personality?', size_hint=(.45, .1), pos_hint={'x': .05, 'y': .5}))
        self.password = TextInput(multiline=False, password=True, size_hint=(.45, .1), pos_hint={'x': .5, 'y': .5})
        self.add_widget(self.password)
        


    #def on_release(self):
        #self.source = 'atlas://data/images/defaulttheme/checkbox_off'




     


class MyApp(App):
    def build(self):
        global sm
        #return StartScreen()
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(RegisterWindow(name='register'))
        sm.add_widget(LoginWindow(name='login'))
        sm.add_widget(InitialQuestion(name='question'))

        sm.current='start'
        
        
        
        
        return sm
        
    



if __name__ == '__main__':

    MyApp().run()