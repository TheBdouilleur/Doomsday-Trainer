# TODO. Quit method of ConfirmWindow
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.core.window import Window


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

