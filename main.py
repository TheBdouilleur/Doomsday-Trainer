# TODO. resultLabel bg = green when correct, else red
# TODO. proper 'Play again' method

import doomsday, logging # Common Conway date operations

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

logging.basicConfig(filename='average.log', level=logging.DEBUG)

class Trainer(App):
    random_date = StringProperty("")
    random_date = doomsday.randomDate()

    results = DictProperty("")
    results = {'text': '', 'correct':None}
    
    answer = StringProperty("")
    

    def build(self):
        return Builder.load_file("trainer.kv")

    def generate_results(self): # TODO reformat function more pythonically (results(self, answer))
        day = str(doomsday.dayFromDate(self.random_date))
    
        if self.answer == day:
            self.results['correct'] = True
            self.results['text'] = 'Congrats!'
            logging.info('New perf: {0} answered in s seconds!'.format(self.random_date))
        
        else:
            self.results['correct'] = True
            self.results['text'] = 'False: real answer was ' + day
            logging.info(' {0} False {1} in s seconds: real answer: {2}'.format(self.random_date, self.results, day))

        self.root.get_screen('third').ids.resultLabel.text = self.results['text'] #Update resultLabel's text
        print('Label text after: ', self.root.get_screen('third').ids.resultLabel.text)


if __name__ == "__main__":
    Trainer().run()

