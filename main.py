from kivy.lang import Builder
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from random import randint
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.size = (360, 600)

screen_helper = """
ScreenManager:
    Menu:
    Welcome:
    Quiz:
    ResultScreen:

<Menu>:
    name: 'menu'
    
    Image:
        source: 'PICTURESZ/415882075_380996107850019_2712619820488601667_n.jpg'  # Replace with the actual path to your image
        allow_stretch: True
        keep_ratio: False
        pos: self.pos
        size: self.size

    MDLabel:
        text: "MIND"
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        font_name: 'font/anton.ttf'
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        font_size: '120sp'
        
    MDLabel:
        text: "MATH"
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        font_name: 'font/anton.ttf'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        font_size: '120sp'   
        
    MDLabel:
        text: "Made by:"
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        font_name: 'font/Aller_Std_Rg.ttf'
        pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        font_size: '20sp'
        
    MDLabel:
        text: "The Rhudz Brothers"
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        font_name: 'font/Inlanders Demo.otf'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        font_size: '20sp'
            
    MDRectangleFlatButton:
        text: 'START'
        font_name: 'font/anton.ttf'
        font_size: '24sp'
        theme_text_color: 'Custom'
        text_color: 0,0,0
        pos_hint: {'center_x': 0.5, 'center_y': 0.325}
        on_press: root.manager.current = "welcome"
        size_hint: 0.5, 0.2       
        md_bg_color: 252/255,186/255,3/255

<Welcome>:
    name: 'welcome'
    
    Image:
        source: 'PICTURESZ/v859-katie-11.jpg'  # Replace with the actual path to your image
        allow_stretch: True
        keep_ratio: False
        pos: self.pos
        size: self.size

    MDLabel:
        text: "WELCOME TO"
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        font_name: 'font/anton.ttf'
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        font_size: '40sp'
        
    MDLabel:
        text: "MIND MATH!"
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        font_name: 'font/anton.ttf'
        pos_hint: {'center_x': 0.5, 'center_y': 0.825}
        font_size: '40sp'    
        
    MDLabel:
        text: "The rules are simple."
        multiline: True
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        font_name: 'font/Aller_Std_Rg.ttf'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}        
        font_size: '18sp'
        
    MDLabel:
        text: "ADD/SUBTRACT/MULTIPLY/DIVIDE" 
        multiline: True
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        font_name: 'font/anton.ttf'
        pos_hint: {'center_x': 0.5, 'center_y': 0.65}
        font_size: '25sp'   
        
    MDLabel:
        text: "as many numbers as you can! "
        multiline: True
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        font_name: 'font/Aller_Std_Rg.ttf'
        font_size: '18sp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6} 
        
    MDLabel:
        text: "Note: For division,"
        multiline: True
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        font_name: 'font/anton.ttf'
        font_size: '18sp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}     
        
    MDLabel:
        text: "round off to first decimal digit."
        multiline: True
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 1,1,1,1
        font_name: 'font/Aller_Std_Rg.ttf'
        font_size: '18sp'
        pos_hint: {'center_x': 0.5, 'center_y': 0.45} 
            
    MDRectangleFlatButton:
        
        text: 'Play!'
        font_name: 'font/anton.ttf'
        font_size: '40sp'
        theme_text_color: 'Custom'
        text_color: 0,0,0
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press: root.manager.current = "KV"
        size_hint: 0.5, 0       
        md_bg_color: 252/255,186/255,3/255
        
    MDRectangleFlatButton:      
        text: 'Back'
        font_name: 'font/anton.ttf'
        font_size: '40sp'
        theme_text_color: 'Custom'
        text_color: 0,0,0
        pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        on_press: root.manager.current = "menu"
        size_hint: 0.5, 0       
        md_bg_color: 252/255,186/255,3/255
        
        
<Quiz>:
    name: 'KV'
    
    Image:
        source: 'Image:
        source: 'PICTURESZ/444ef0ffe923fdc13acfe4f429774c2a.jpg' 
        allow_stretch: True
        keep_ratio: False
        pos: self.pos
        size: self.size'  # Replace with the actual path to your image
        allow_stretch: True
        keep_ratio: False
        pos: self.pos
        size: self.size
    
    BoxLayout:
        orientation: 'vertical'
        MDRectangleFlatButton:
            text: 'BACK TO MENU'
            font_size: '24sp'
            font_name: 'font/anton.ttf'
            theme_text_color: 'Custom'
            text_color: 0,0,0
            md_bg_color: 252/255,186/255,3/255
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            on_press: root.manager.current = "menu"


        MDLabel:
            id: question_label
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 1,1,1
            font_name: 'font/anton.ttf'
            font_size: '60sp'

        MDTextField:
            mode: "fill"
            width: "250sp"
            height: "200sp"
            size_hint_x: None
            id: answer_input
            hint_text: "Enter your answer:"   
            hint_text_mode: "on_focus"     
            icon_right: "numeric"
            input_type: 'number'
            multiline: False
            halign: 'center'
            on_text_validate: app.check_answer()           
            pos_hint: {'center_x': 0.5, 'center_y': 0.35}

        BoxLayout:
            orientation: 'horizontal'
            spacing: '10dp'
            size_hint_y: None
            height: '48dp'

        FloatLayout:
            MDRectangleFlatButton:
                text: "SUBMIT"
                font_size: '24sp'
                font_name: 'font/anton.ttf'
                theme_text_color: 'Custom'
                text_color: 0,0,0
                md_bg_color: 252/255,186/255,3/255
                on_press: app.check_answer()
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}
                size_hint: 0.5, 0.2

            MDRectangleFlatButton:
                text: "NEW QUESTION"
                font_size: '24sp'
                font_name: 'font/anton.ttf'
                theme_text_color: 'Custom'
                text_color: 0,0,0
                md_bg_color: 252/255,186/255,3/255                
                on_press: app.next_question()
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: 0.5, 0.2

<ResultScreen>:
    name: 'result'
    FloatLayout:
        
        Image:
            source: 'Image:
            source: 'PICTURESZ/v859-katie-11.jpg' 
            allow_stretch: True
            keep_ratio: False
            pos: self.pos
            

        MDLabel:
            id: result_label
            font_name: 'font/anton.ttf'
            font_size: '18sp'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 1,1,1

        MDRaisedButton:
            text: "Play Again"            
            font_size: '30sp'
            font_name: 'font/anton.ttf'
            theme_text_color: 'Custom'
            text_color: 0,0,0
            md_bg_color: 252/255,186/255,3/255                
            on_press: app.next_question()
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}
            size_hint: 0.5, 0
            on_press: app.play_again()

"""

class Menu(Screen):
    pass

class Welcome(Screen):
    pass
class Quiz(Screen):
    pass
class ResultScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Welcome(name='welcome'))
sm.add_widget(Menu(name='menu'))
sm.add_widget(Quiz(name='KV'))
sm.add_widget(ResultScreen(name='result'))

class MathQuizApp(MDApp):
    def build(self):
        return Builder.load_string(screen_helper)

    def on_start(self):
        self.question_label = self.root.get_screen('KV').ids.question_label
        self.answer_input = self.root.get_screen('KV').ids.answer_input
        self.result_label = self.root.get_screen('result').ids.result_label
        self.correct_answer = None
        self.generate_question()


    def generate_question(self):
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        operation = randint(1, 3)

        if operation == 1:
            self.correct_answer = num1 + num2
            question_text = f"{num1} + {num2} = ?"
        elif operation == 2:
            self.correct_answer = num1 - num2
            question_text = f"{num1} - {num2} = ?"
        else:
            while num2 == 0:
                num2 = randint(1, 10)
            if num1 % 2 != 0:
                num1 += 1
            if num2 % 2 != 0:
                num2 += 1


            self.correct_answer = round(num1 / num2,1)
            question_text = f"{num1} / {num2} = ?"

        self.question_label.text = question_text
        self.answer_input.text = ""

    def check_answer(self):
        try:
            user_answer = float(self.answer_input.text)
            if user_answer == self.correct_answer:
                self.show_result("Correct! Well done!", (0, 1, 0, 1))  # Green color for correct answer
            else:
                self.show_result(f"Incorrect! Correct answer is {self.correct_answer}.",
                                 (1, 0, 0, 1))  # Red color for incorrect answer
        except ValueError:
            self.show_result("Invalid input! Please enter a number.", (1, 0, 0, 1))  # Red color for invalid input

    def show_result(self, result_text, color):
        self.result_label.text = result_text
        self.root.current = 'result'

    def next_question(self):
        self.root.current = 'KV'
        self.generate_question()

    def play_again(self):
        self.root.current = 'KV'
        self.generate_question()

if __name__ == '__main__':
    MathQuizApp().run()