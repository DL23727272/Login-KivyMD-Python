from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

class testApp(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Yellow"
        
        return testApp() 

if __name__ == "__main__":
    Window.size = (360, 640)
    Builder.load_file("main.kv")
    MyApp().run()