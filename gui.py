# TODO. Quit method of StartWindow
import os
os.environ['KIVY_GL_BACKEND'] = 'sdl2' # Change the backend to avoid a Linux error 

import doomsday # Common Conway date operations

import kivy  # Kivy different modules
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty, DictProperty


class StartWindow(Screen):
    pass


class DateWindow(Screen):
    pass


class ResultWindow(Screen):
    def init():
        pass



class WindowManager(ScreenManager):
    pass



date = "Hello"
WIDTH = 400
HEIGHT = 200

kivy.require('1.10.1')
Config.set('graphics', 'width', str(WIDTH))
Config.set('graphics', 'height', str(HEIGHT))
Config.write()


class Trainer(App):
    random_date = StringProperty("")
    answer = StringProperty("")
    results = StringProperty("") # DictProperty("")
    results = 'no r yet' # {'text': 'no results yet'}
    #def resize(self):
        #Window.size = (WIDTH+1, HEIGHT)

    def build(self):
        self.random_date = doomsday.randomDate()

        return Builder.load_file("trainer.kv")

    def get_answer(self):
        print("answerfromtrainer:", self.answer)
        results = 'hi'+ self.answer # ['text']
        print(results)


if __name__ == "__main__":
    Trainer().run()

