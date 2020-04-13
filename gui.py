# TODO. Quit method of ConfirmWindow
import os
os.environ['KIVY_GL_BACKEND'] = 'sdl2' # Change the backend to avoid a Linux error 
from kivy.core.window import Window

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty

class ConfirmWindow(Screen):
    pass


class DateWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


date = "Hello"
WIDTH = 400
HEIGHT = 200

kivy.require('1.11.1')
Config.set('graphics', 'width', str(WIDTH))
Config.set('graphics', 'height', str(HEIGHT))
Config.write()


class Trainer(App):
    date = StringProperty("")

    def resize(self):
        Window.size = (WIDTH+1, HEIGHT)

    def build(self):
        self.date = "coucou"
        kv = Builder.load_file("trainer.kv")
        return kv


def quit():
    print('quit')


if __name__ == "__main__":
    Trainer().run()

