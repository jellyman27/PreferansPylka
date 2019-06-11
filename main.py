from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivymd.button import MDFlatButton
import os
import re
import sqlite3

Builder.load_string("""
#:kivy 1.10.1

<MainMenu>:
    canvas:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
            source: "main_bgr.jpg"
    FloatLayout:
        AnchorLayout:
            anchor_x: 'left'
            BoxLayout:
                padding: 10
                size_hint : .6, .4
                spacing : root.width / 20
                orientation: 'vertical'
                Button:
                    background_color: 1, 0.5, 0.25, 1
                    text: 'Продолжить игру'
                    on_press: root.load_game()
                Button:
                    background_color: 1, 0.5, 0.25, 1
                    text: 'Новая игра'
                    on_press: root.manager.current = 'newgame'
                Button: 
                    background_color: 1, 0.5, 0.25, 1
                    text: 'Статистика'
                    on_press: root.manager.current = 'stats'
<NewGameMenu>
    canvas:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
            source: "main_bgr.jpg"
    AnchorLayout:
        BoxLayout:
            spacing : 5
            orientation: 'vertical'
            padding: 50, 20
            TextInput:
                id: name1
                padding_x: 40
                font_size: 20
                hint_text: 'Имя первого игрока'
                size_hint: 1, 0.3
            TextInput:
                id:name2
                padding_x: 40
                font_size: 20
                hint_text: 'Имя второго игрока'
                size_hint: 1, 0.3
            TextInput:
                id:name3
                padding_x: 40
                font_size: 20
                hint_text: 'Имя третьего игрока'
                size_hint: 1, 0.3
            TextInput:
                id:name4
                padding_x: 40
                font_size: 20
                hint_text: 'Имя четвёртого игрока(если нужно)'
                size_hint: 1, 0.3
            AnchorLayout:
            	anchor_x: "center"
            	anchor_y: "bottom"
            	BoxLayout:
                    spacing : 5
                    size_hint: 1, .4
                    orientation: 'vertical'
            	    Button:
            	        background_color: 1, 0.5, 0.25, 1
            		    text: 'Начать игру'
                	    on_press: root.submit_name()
                	Button:
            	        background_color: 1, 0.5, 0.25, 1
            		    text: 'Меню'
                	    on_press: root.manager.current = 'menu'
                	
<GameScreen3>
    Widget:
        id: game_screen3
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
            Color:
                rgba: 0, 0, 0, 1
            Line:
                points: 0, 0, self.width / 2, self.height / 2
            Line:
                points: self.width / 2,self.height / 2,self.width, 0
            Line:
                points: self.width / 2,self.height / 2,self.width / 2, self.height
            Line:
                points: self.width / 10, self.height, self.width / 10, self.height / 10, self.width -self.width / 10, self.height / 10, self.width -self.width / 10, self.height
            Line:
                points: self.width / 20, self.height, self.width / 20, self.height / 20, self.width - self.width / 20, self.height / 20, self.width - self.width / 20, self.height
            Line:
                points: 0, self.height / 2, self.width / 20, self.height / 2
            Line:
                points: self.width / 2, 0, self.width / 2, self.height / 20
            Line:
                points: self.width - self.width / 20, self.height / 2, self.width, self.height / 2
            Color:
                rgba: 1, 1, 1, 1
            Ellipse:
                pos: self.width / 2 - self.width / 20, self.height / 2 - self.width / 20
                size: self.width / 10, self.width / 10
            Color:
                rgba: 0, 0, 0, 1
            Line:
                circle: self.width / 2, self.height / 2 , self.width / 20
        Button:
            id: button1
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 30
            text: "0"
            pos: root.width / 2 - root.width / 40, root.height / 2-root.width / 40
            size: root.width / 20,root.height / 20
            on_press: app.update_pulya(self)
        Button:
            id: vist_1_3
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: 0, root.height / 2
            size: root.width / 20, root.height / 2
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id:vist_1_2
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: 0, root.height / 20
            size: root.width / 20, root.height / 2-root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: pylya_1
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width / 20, root.height / 10
            size: root.width / 20, root.height - root.height / 10
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id:gora_1
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width / 10, root.height / 10 + root.height / 20
            size: root.width / 20, root.height - root.height / 10 - root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: vist_2_1
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width / 20, 0
            size: root.width / 2 - root.width / 20, root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: vist_2_3
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width / 2, 0
            size: root.width / 2 - root.width / 20, root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: pylya_2
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width / 10, root.height / 20
            size: root.width-root.width / 5, root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: gora_2
            background_color:1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width / 10 + root.width / 20, root.height / 10
            size:root.width - root.width / 2 + root.width / 4 - root.width / 20, root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: vist_3_1
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width - root.width / 20,root.height / 2
            size: root.width / 20, root.height / 2
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: pylya_3
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width - root.width / 10, root.height / 10
            size: root.width / 20, root.height - root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: vist_3_2
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width - root.width / 20, root.height / 20
            size: root.width / 20, root.height / 2 - root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id:gora_3
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width - root.width / 10 - root.width / 20, root.height / 10 + root.height / 20
            size: root.width / 20, root.height - root.height / 20 - root.height / 10
            on_press: app.update_num(self)
            text_size: self.size
        Label:
            id: label1
            color: 0, 0, 0, 1
            font_size : 15
            text: "NAME1"
            pos: root.width / 4, root.height / 2
            size: root.width / 20, root.height / 20
        Label:
            id:label2
            color: 0, 0, 0, 1
            font_size : 15
            text: "NAME2"
            pos: root.width * 3 / 4, root.height / 2
            size: root.width / 20, root.height / 20
        Label:
            id:label3
            color: 0, 0, 0, 1
            font_size : 15
            text: "NAME3"
            pos: root.width / 2, root.height / 4
            size: root.width / 20, root.height / 20
        Button:
            id: button_end_game
            background_color: 1, 0, 1, 1
            font_size: 15
            text: "Расчитать пулю"
            pos: root.width / 2 - self.width / 2, root.height / 3 * 2 - self.height  / 2
            size: root.width / 5, root.height / 20
            on_press: root.end_game()
        Button:
            id: button_menu
            background_color: 1, 0, 1, 1
            font_size: 15
            text: "Меню"
            pos: root.width / 2 - self.width / 2, root.height / 3 * 2.2 - self.height / 2
            size: root.width / 5, root.height / 20
            on_press: root.manager.current = "menu"


<GameScreen4>
    Widget:
        id: game_screen4
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size
            Color:
                rgba: 0, 0, 0, 1
            Line:
                points: 0, 0, self.width, self.height
            Line:
                points: 0, self.height, self.width, 0
            Line:
                points: self.width / 10, self.height - self.height / 10, self.width / 10, self.height / 10, self.width - self.width / 10, self.height / 10, self.width - self.width / 10, self.height - self.height / 10, self.width / 10, self.height - self.height / 10
            Line:
                points: self.width / 20, self.height - self.height / 20, self.width / 20, self.height / 20, self.width - self.width / 20, self.height / 20, self.width - self.width / 20, self.height - self.height / 20, self.width / 20, self.height - self.height / 20
            Line:
                points: 0, self.height / 3, self.width / 20, self.height / 3
            Line:
                points: 0, self.height * 2 / 3, self.width / 20, self.height * 2 / 3
            Line:
                points: self.width / 3, 0, self.width / 3, self.height / 20
            Line:
                points: self.width * 2 / 3, 0, self.width * 2 / 3, self.height / 20
            Line:
                points: self.width - self.width / 20, self.height / 3, self.width, self.height / 3
            Line:
                points: self.width - self.width / 20, self.height * 2 / 3, self.width, self.height * 2 / 3
            Line:
                points: self.width / 3, self.height, self.width / 3,self.height - self.height / 20
            Line:
                points: self.width * 2 / 3, self.height, self.width * 2 / 3, self.height - self.height / 20
            Color:
                rgba: 1, 1, 1, 1
            Ellipse:
                pos: self.width / 2 - self.width / 20, self.height / 2 - self.width / 20
                size: self.width / 10, self.width / 10
            Color:
                rgba: 0, 0, 0, 1
            Line:
                circle: self.width / 2, self.height / 2 , self.width / 20
        Button:
            id: button1
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 30
            text: "0"
            pos: root.width / 2 - root.width / 40, root.height / 2 - root.width / 40
            size: root.width / 20,root.height / 20
            on_press: app.update_pulya(self)
        Button:
            id: vist_1_3
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: 0, root.height / 3
            size: root.width / 20, root.height / 3
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id:vist_1_2
            background_color:1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: 0, root.height / 20
            size: root.width / 20, root.height / 3-root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id:vist_1_4
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: 0, root.height * 2 / 3
            size: root.width / 20, root.height / 3-root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: pylya_1
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width / 20, root.height / 10
            size: root.width / 20, root.height - root.height / 5
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id:gora_1
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width / 10, root.height / 10 + root.height / 20
            size: root.width / 20, root.height-root.height / 5 - root.height / 10
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: vist_2_1
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width / 20, 0
            size: root.width / 3 - root.width / 20, root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: vist_2_3
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width * 2 / 3, 0
            size: root.width / 3 - root.width / 20, root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: vist_2_4
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width  / 3, 0
            size: root.width / 3, root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: pylya_2
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width / 10, root.height / 20
            size: root.width-root.width / 5, root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: gora_2
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width / 10+root.width / 20, root.height / 10
            size:root.width-root.width / 2 + root.width / 4 - root.width / 20, root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: vist_3_1
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width - root.width / 20,root.height / 3
            size: root.width / 20, root.height / 3
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: pylya_3
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width - root.width / 10, root.height / 10
            size: root.width / 20, root.height-root.height / 10
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: vist_3_2
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width-root.width / 20, root.height / 20
            size: root.width / 20, root.height / 3-root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: vist_3_4
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width-root.width / 20, root.height * 2 / 3
            size: root.width / 20, root.height / 3-root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id:gora_3
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width - root.width / 10 - root.width / 20, root.height / 10 + root.height / 20
            size: root.width / 20, root.height - root.height / 10 - root.height / 5
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: vist_4_1
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width / 20, root.height - root.height / 20
            size: root.width / 3 - root.width / 20, root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: vist_4_3
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width * 2 / 3, root.height - root.height / 20
            size: root.width / 3 - root.width / 20, root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: vist_4_2
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width  / 3, root.height - root.height / 20
            size: root.width / 3, root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: pylya_4
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width / 10, root.height - root.height / 10
            size: root.width-root.width / 5, root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Button:
            id: gora_4
            background_color: 1, 1, 1, 0
            color: 0, 0, 0, 1
            font_size : 15
            text: "0"
            pos: root.width / 10 + root.width / 20, root.height - root.height  / 5 + root.height / 20
            size:root.width-root.width / 2 + root.width / 4 - root.width / 20, root.height / 20
            on_press: app.update_num(self)
            text_size: self.size
        Label:
            id: label1
            color: 0, 0, 0, 1
            font_size : 15
            text: "NAME1"
            pos: root.width / 4, root.height / 2
            size: root.width / 20, root.height / 20
        Label:
            id: label3
            color: 0, 0, 0, 1
            font_size : 15
            text: "NAME3"
            pos: root.width * 3 / 4,root.height / 2
            size: root.width / 20, root.height / 20
        Label:
            id: label2
            color: 0, 0, 0, 1
            font_size : 15
            text: "NAME2"
            pos: root.width / 2, root.height / 4
            size: root.width / 20, root.height / 20
        Label:
            id: label4
            color: 0, 0, 0, 1
            font_size : 15
            text: "NAME4"
            pos: root.width / 2, root.height - root.height / 4
            size: root.width / 20, root.height / 20
        Button:
            id: button_end_game
            background_color: 1, 0, 1, 1
            font_size: 15
            text: "Расчитать пулю"
            pos: root.width / 2 - self.width / 2, root.height / 3 * 2 - self.height / 2
            size: root.width / 5, root.height / 20
            on_press: root.end_game()
        Button:
            id: button_menu
            background_color: 1, 0, 1, 1
            font_size: 15
            text: "Меню"
            pos: root.width / 2 - self.width / 2, root.height / 3 * 2.15 - self.height / 2
            size: root.width / 5, root.height / 20
            on_press: root.manager.current = "menu"


<StatsMenu>:
    AnchorLayout:
        BoxLayout:
            size_hint : .8, .6
            spacing : root.width / 20
            orientation: 'vertical'
            BoxLayout:
                orientation: 'vertical'
                BoxLayout:
                    orientation: 'vertical'
                    BoxLayout:
                        Label:
                            id: player1
                            text:"NAME1"
                        Label:
                            id: stats1
                            text:"StatName1"
                    BoxLayout:
                        Label:
                            id: player2
                            text:"NAME2"
                        Label:
                            id: stats2
                            text:"StatName2"
                    BoxLayout:
                        Label:
                            id: player3
                            text:"NAME3"
                        Label:
                            id: stats3
                            text:"StatName3"
                    BoxLayout:
                        Label:
                            id: player4
                            text:"NAME4"
                        Label:
                            id: stats4
                            text:"StatName4"
            BoxLayout:
                size_hint: 1, .2
                spacing: .045
                Button:
                    on_press: root.update_left()
                    text:"<="
                Button:
                    text: 'Меню'
                    on_press: root.manager.current = 'menu'
                Button:
                    on_press: root.update_right()
                    text:"=>"

<MyPopup>:
    BoxLayout:
        orientation: 'vertical'
        TextInput:
            id:text1
            text: ""
        Button:
            text: "Ok!"
            on_release: root.dismiss()
""")

class MainMenu(Screen):
        #<----------------считывание_файла_c_последней_игрой----------------->
    def load_game(self):
        fileload = open("load.txt", 'r')
        namegame = fileload.readline()
        if namegame == "game3\n":
            player1 = fileload.readline()
            pylya1 = fileload.readline()
            gora1 = fileload.readline()
            vist1_2 = fileload.readline()
            vist1_3 = fileload.readline()
            player2 = fileload.readline()
            pylya2 = fileload.readline()
            gora2 = fileload.readline()
            vist2_1 = fileload.readline()
            vist2_3 = fileload.readline()
            player3 = fileload.readline()
            pylya3 = fileload.readline()
            gora3 = fileload.readline()
            vist3_1 = fileload.readline()
            vist3_2 = fileload.readline()
            fileload.close()
            gamescreen3 = sm.get_screen("game3")
            gamescreen3.ids.label1.text = player1[:-1]
            gamescreen3.ids.label2.text = player2[:-1]
            gamescreen3.ids.label3.text = player3[:-1]
            gamescreen3.ids.pylya_1.text = pylya1[:-1]
            gamescreen3.ids.pylya_2.text = pylya2[:-1]
            gamescreen3.ids.pylya_3.text = pylya3[:-1]
            gamescreen3.ids.gora_1.text = gora1[:-1]
            gamescreen3.ids.gora_2.text = gora2[:-1]
            gamescreen3.ids.gora_3.text = gora3[:-1]
            gamescreen3.ids.vist_1_2.text = vist1_2[:-1]
            gamescreen3.ids.vist_1_3.text = vist1_3[:-1]
            gamescreen3.ids.vist_2_1.text = vist2_1[:-1]
            gamescreen3.ids.vist_2_3.text = vist2_3[:-1]
            gamescreen3.ids.vist_3_1.text = vist3_1[:-1]
            gamescreen3.ids.vist_3_2.text = vist3_2[:-1]
            sm.current = "game3"
        elif namegame == "game4\n":
            player1 = fileload.readline()
            pylya1 = fileload.readline()
            gora1 = fileload.readline()
            vist1_2 = fileload.readline()
            vist1_3 = fileload.readline()
            vist1_4 = fileload.readline()
            player2 = fileload.readline()
            pylya2 = fileload.readline()
            gora2 = fileload.readline()
            vist2_1 = fileload.readline()
            vist2_3 = fileload.readline()
            vist2_4 = fileload.readline()
            player3 = fileload.readline()
            pylya3 = fileload.readline()
            gora3 = fileload.readline()
            vist3_1 = fileload.readline()
            vist3_2 = fileload.readline()
            vist3_4 = fileload.readline()
            player4 = fileload.readline()
            pylya4 = fileload.readline()
            gora4 = fileload.readline()
            vist4_1 = fileload.readline()
            vist4_2 = fileload.readline()
            vist4_3 = fileload.readline()
            fileload.close()
            gamescreen4 = sm.get_screen("game4")
            gamescreen4.ids.label1.text = player1[:-1]
            gamescreen4.ids.label2.text = player2[:-1]
            gamescreen4.ids.label3.text = player3[:-1]
            gamescreen4.ids.label4.text = player4[:-1]
            gamescreen4.ids.pylya_1.text = pylya1[:-1]
            gamescreen4.ids.pylya_2.text = pylya2[:-1]
            gamescreen4.ids.pylya_3.text = pylya3[:-1]
            gamescreen4.ids.pylya_4.text = pylya4[:-1]
            gamescreen4.ids.gora_1.text = gora1[:-1]
            gamescreen4.ids.gora_2.text = gora2[:-1]
            gamescreen4.ids.gora_3.text = gora3[:-1]
            gamescreen4.ids.gora_4.text = gora4[:-1]
            gamescreen4.ids.vist_1_2.text = vist1_2[:-1]
            gamescreen4.ids.vist_1_3.text = vist1_3[:-1]
            gamescreen4.ids.vist_1_4.text = vist1_4[:-1]
            gamescreen4.ids.vist_2_1.text = vist2_1[:-1]
            gamescreen4.ids.vist_2_3.text = vist2_3[:-1]
            gamescreen4.ids.vist_2_4.text = vist2_4[:-1]
            gamescreen4.ids.vist_3_1.text = vist3_1[:-1]
            gamescreen4.ids.vist_3_2.text = vist3_2[:-1]
            gamescreen4.ids.vist_3_4.text = vist3_4[:-1]
            gamescreen4.ids.vist_4_1.text = vist4_1[:-1]
            gamescreen4.ids.vist_4_2.text = vist4_2[:-1]
            gamescreen4.ids.vist_4_3.text = vist4_3
            sm.current = "game4"
        else:
            pass

class StatsMenu(Screen):
    lastnumber = None
    number = 1
    def update_right(self):
        print(self.number);
        self.number+=1;
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        sql = "select numbers FROM stats ORDER BY numbers DESC LIMIT 1"
        cursor.execute(sql)
        firstgame = cursor.fetchall()
        if firstgame!= []:
            self.lastnumber = firstgame.pop()[0]
            if (self.number > self.lastnumber):
                self.number = 1;
            sql = "SELECT * FROM stats WHERE numbers=?"
            cursor.execute(sql, str(self.number))
            firstgame = cursor.fetchall().pop()
            gamestats = sm.get_screen('stats')
            gamestats.ids.player1.text = firstgame[1]
            gamestats.ids.stats1.text = firstgame[2]
            gamestats.ids.player2.text = firstgame[1]
            gamestats.ids.stats2.text = firstgame[3]
            gamestats.ids.player3.text = firstgame[4]
            gamestats.ids.stats3.text = firstgame[5]
            gamestats.ids.player4.text = firstgame[6]
            gamestats.ids.stats4.text = firstgame[7]
            
    def update_left(self):
        print(self.number)
        self.number-=1;
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        sql = "select numbers FROM stats ORDER BY numbers DESC LIMIT 1"
        cursor.execute(sql)
        firstgame = cursor.fetchall()
        if firstgame!= []:
            self.lastnumber = firstgame.pop()[0]
            if (self.number < 1):
                self.number = self.lastnumber;
            sql = "SELECT * FROM stats WHERE numbers=?"
            cursor.execute(sql, str(self.number))
            firstgame = cursor.fetchall().pop()
            gamestats = sm.get_screen('stats')
            gamestats.ids.player1.text = firstgame[1]
            gamestats.ids.stats1.text = firstgame[2]
            gamestats.ids.player2.text = firstgame[1]
            gamestats.ids.stats2.text = firstgame[3]
            gamestats.ids.player3.text = firstgame[4]
            gamestats.ids.stats3.text = firstgame[5]
            gamestats.ids.player4.text = firstgame[6]
            gamestats.ids.stats4.text = firstgame[7]

    
    
class NewGameMenu(Screen):
    def submit_name(self):
        gamescreen3 = sm.get_screen("game3")
        gamescreen4 = sm.get_screen("game4")
        new_game = sm.get_screen("newgame")
        if (new_game.ids.name4.text == "") and (new_game.ids.name1.text!="") and(new_game.ids.name2.text != "") and (new_game.ids.name3.text != "") :
            gamescreen3.ids.label1.text = new_game.ids.name1.text
            gamescreen3.ids.label2.text = new_game.ids.name2.text
            gamescreen3.ids.label3.text = new_game.ids.name3.text
            sm.current = "game3"
        elif (new_game.ids.name4.text != "") and (new_game.ids.name1.text!="") and(new_game.ids.name2.text != "") and (new_game.ids.name3.text != ""):
            gamescreen4.ids.label1.text = new_game.ids.name1.text
            gamescreen4.ids.label2.text = new_game.ids.name2.text
            gamescreen4.ids.label3.text = new_game.ids.name3.text
            gamescreen4.ids.label4.text = new_game.ids.name4.text
            sm.current = "game4"
        else:
            pass
            
class GameScreen3(Screen):
    def end_game(self):
        gamescreen3 = sm.get_screen("game3")
        pylya1= int(re.findall('[\d]+', gamescreen3.ids.pylya_1.text).pop())
        pylya2= int(re.findall('[\d]+', gamescreen3.ids.pylya_2.text).pop())
        pylya3= int(re.findall('[\d]+', gamescreen3.ids.pylya_3.text).pop())
        pylka = int(re.findall('[\d]+', gamescreen3.ids.button1.text).pop())
        if (pylya1== pylka) and (pylya2== pylka) and (pylya3== pylka):
            vist = int(re.findall('[\d]+',gamescreen3.ids.vist_2_1.text).pop())
            vist_1_2 = int(re.findall('[\d]+',gamescreen3.ids.vist_1_2.text).pop())
            vist_1_2 = vist_1_2 - vist
            vist = int(re.findall('[\d]+',gamescreen3.ids.vist_3_1.text).pop())
            vist_1_3 = int(re.findall('[\d]+',gamescreen3.ids.vist_1_3.text).pop())
            vist_1_3 = vist_1_3 - vist
            vist = int(re.findall('[\d]+',gamescreen3.ids.vist_3_2.text).pop())
            vist_2_3 = int(re.findall('[\d]+',gamescreen3.ids.vist_2_3.text).pop())
            vist_2_3 = vist_2_3 - vist
            player1 = vist_1_2 + vist_1_3
            player2 = (-1)*vist_1_2 + vist_2_3
            player3 = (-1)*vist_1_3 + (-1)*vist_2_3
            mingora = 0
            oldgora1 = int(re.findall('[\d]+',gamescreen3.ids.gora_1.text).pop())
            oldgora2 = int(re.findall('[\d]+',gamescreen3.ids.gora_2.text).pop())
            oldgora3 = int(re.findall('[\d]+',gamescreen3.ids.gora_3.text).pop())
            if (oldgora1 < oldgora2):
                if (oldgora1 < oldgora3):
                    mingora = oldgora1
                else:
                    mingora = oldgora3
            else:
                if (oldgora2 < oldgora3):
                    mingora = oldgora2
                else:
                    mingora = oldgora3
            oldgora1 -= mingora
            oldgora2 -= mingora
            oldgora3 -= mingora
            gora1_3 = oldgora1-oldgora3
            gora1_2 = oldgora1-oldgora2
            gora1 = (-1) * (gora1_3+gora1_2) * (10 / 3)
            gora2_1 = oldgora2 - oldgora1
            gora2_3 = oldgora2 - oldgora3
            gora2 = (-1) * (gora2_1+gora2_3) * (10 / 3)
            gora3_1 = oldgora3 - oldgora1
            gora3_2 = oldgora3 - oldgora2
            gora3 = (-1) * (gora3_1 + gora3_2) * (10 / 3)
            player1 += gora1
            player2 += gora2
            player3 += gora3
            #--------------------------внос результатов в бд------------------
            conn = sqlite3.connect("mydatabase.db")
            cursor = conn.cursor()
            sql = "select numbers FROM stats ORDER BY numbers DESC LIMIT 1"
            cursor.execute(sql)
            lastnumber = 0;
            lol = cursor.fetchall()
            if lol!= []:
                lastnumber = lol.pop()[0]
            stats = [str(lastnumber+1),gamescreen3.ids.label1.text ,str(player1),gamescreen3.ids.label2.text , str(player2),gamescreen3.ids.label3.text , str(player3),'NONE' ,'NONE']
            cursor.execute("INSERT INTO stats VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", stats)
            conn.commit()
            #---------------------------отображение результатов----------------
            gamescreen3.ids.label1.text+=("\n"+str(player1))
            gamescreen3.ids.label2.text+=("\n"+str(player3))
            gamescreen3.ids.label3.text+=("\n"+str(player2))
        
class GameScreen4(Screen):
    def end_game(self):
        gamescreen4 = sm.get_screen("game4")
        pylya1= int(re.findall('[\d]+', gamescreen4.ids.pylya_1.text).pop())
        pylya2= int(re.findall('[\d]+', gamescreen4.ids.pylya_2.text).pop())
        pylya3= int(re.findall('[\d]+', gamescreen4.ids.pylya_3.text).pop())
        pylya4= int(re.findall('[\d]+', gamescreen4.ids.pylya_4.text).pop())
        pylka = int(re.findall('[\d]+', gamescreen4.ids.button1.text).pop())
        if (pylya1== pylka) and (pylya2== pylka) and (pylya3== pylka) and (pylya4 == pylka):
            vist1_2 = int(re.findall('[\d]+', gamescreen4.ids.vist_1_2.text).pop())
            vist1_3 = int(re.findall('[\d]+', gamescreen4.ids.vist_1_3.text).pop())
            vist1_4 = int(re.findall('[\d]+', gamescreen4.ids.vist_1_4.text).pop())
            vist2_1 = int(re.findall('[\d]+', gamescreen4.ids.vist_2_1.text).pop())
            vist3_1 = int(re.findall('[\d]+', gamescreen4.ids.vist_3_1.text).pop())
            vist4_1 = int(re.findall('[\d]+', gamescreen4.ids.vist_4_1.text).pop())
            player1 = vist1_2 - vist2_1
            player1 += vist1_3 - vist3_1
            player1 += vist1_4 - vist4_1
            vist2_3 = int(re.findall('[\d]+', gamescreen4.ids.vist_2_3.text).pop())
            vist2_4 = int(re.findall('[\d]+', gamescreen4.ids.vist_2_4.text).pop())
            vist3_2 = int(re.findall('[\d]+', gamescreen4.ids.vist_3_2.text).pop())
            vist4_2 = int(re.findall('[\d]+', gamescreen4.ids.vist_4_2.text).pop())
            player2 = vist2_1 - vist1_2
            player2 += vist2_3 - vist3_2
            player2 += vist2_4 - vist4_2
            vist3_4 = int(re.findall('[\d]+', gamescreen4.ids.vist_3_4.text).pop())
            vist4_3 = int(re.findall('[\d]+', gamescreen4.ids.vist_4_3.text).pop())
            player3 = vist3_1 - vist1_3
            player3 += vist3_2 - vist2_3
            player3 += vist3_4 - vist4_3
            player4 = vist4_1 - vist1_4
            player4 += vist4_2 - vist2_4
            player4 += vist4_3 - vist3_4
            oldgora1 = int(re.findall('[\d]+', gamescreen4.ids.gora_1.text).pop())
            oldgora2 = int(re.findall('[\d]+', gamescreen4.ids.gora_2.text).pop())
            oldgora3 = int(re.findall('[\d]+', gamescreen4.ids.gora_3.text).pop())
            oldgora4 = int(re.findall('[\d]+', gamescreen4.ids.gora_4.text).pop())
            masgora = [oldgora1, oldgora2, oldgora3, oldgora4]
            mingora = oldgora1
            for i in masgora:
                if i < mingora:
                    mingora = i
            oldgora1 -=mingora
            oldgora2 -=mingora
            oldgora3 -=mingora
            oldgora4 -=mingora
            gora1_2 = oldgora1 - oldgora2
            gora1_3 = oldgora1 - oldgora3
            gora1_4 = oldgora1 - oldgora4
            player1 += (-1) * (gora1_2 + gora1_3 + gora1_4) * (10 / 4)
            gora2_3 = oldgora2 - oldgora3
            gora2_4 = oldgora2 - oldgora4
            player2 +=(-1) * ((-1) * gora1_2 + gora2_3 + gora2_4) * (10/4)
            gora3_4 = oldgora3 - oldgora4
            player3 += (-1) * ((-1) * gora1_3 + (-1) * gora2_3 + gora3_4) * (10/4)
            player4 += (gora1_4 + gora2_4 + gora3_4) * (10/4)
            #--------------------------внос результатов в бд------------------
            conn = sqlite3.connect("mydatabase.db")
            cursor = conn.cursor()
            lastnumber = 0;
            lol = cursor.fetchall() 
            if lol!= []:
                lastnumber = lol.pop()[0]
            stats = [str(lastnumber+1),gamescreen4.ids.label1.text ,str(player1),gamescreen4.ids.label2.text , str(player2),gamescreen4.ids.label3.text , str(player3),gamescreen4.ids.label4.text ,str(player4)]
            cursor.execute("INSERT INTO stats VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", stats)
            conn.commit()
            #---------------------------отображение результатов----------------
            gamescreen4.ids.label1.text+=("\n"+str(player1))
            gamescreen4.ids.label2.text+=("\n"+str(player2))
            gamescreen4.ids.label3.text+=("\n"+str(player3))
            gamescreen4.ids.label4.text+=("\n"+str(player4))
            
class MyPopup(Popup):
    pass

sm = ScreenManager()
sm.add_widget(MainMenu(name='menu'))
sm.add_widget(StatsMenu(name='stats'))
sm.add_widget(NewGameMenu(name='newgame'))
sm.add_widget(GameScreen3(name='game3'))
sm.add_widget(GameScreen4(name='game4'))

class MyApp(App):
    value = ""
    instance = None
    def build(self):
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        sql = "select * FROM stats ORDER BY numbers  LIMIT 1"
        cursor.execute(sql)
        firstgame = cursor.fetchall()
        if firstgame!= []:
            firstgame = firstgame.pop()
            gamestats = sm.get_screen('stats')
            gamestats.ids.player1.text = firstgame[1]
            gamestats.ids.stats1.text = firstgame[2]
            gamestats.ids.player2.text = firstgame[3]
            gamestats.ids.stats2.text = firstgame[4]
            gamestats.ids.player3.text = firstgame[5]
            gamestats.ids.stats3.text = firstgame[6]
            gamestats.ids.player4.text = firstgame[7]
            gamestats.ids.stats4.text = firstgame[8]
            
        return sm

    def update_num(self, instance):
        self.instance = instance
        def my_dismiss(instance):
            self.value = instance.ids.text1.text
            result = re.findall('[\d]+',self.instance.text)
            result =result.pop()
            if self.value == '':
                return False
            self.value = int(self.value) + int(result)
            string1= "."
            string1+=str(self.value)
            self.instance.text+=string1
            #<------------------создание_файла_после_каждого_нажатия----------структура:игрок1\nсчётигрок2\nсчётигрок3\nсчётигрок4(проверка sm)\nсчёт>
            if sm.current == "game3":
                fileload = open("load.txt", 'w')
                gamescreen3 = sm.get_screen("game3")
                name1 = gamescreen3.ids.label1.text
                name2 = gamescreen3.ids.label2.text
                name3 = gamescreen3.ids.label3.text
                pylya1 = (re.findall('[\d]+', gamescreen3.ids.pylya_1.text).pop())
                pylya2 = (re.findall('[\d]+', gamescreen3.ids.pylya_2.text).pop())
                pylya3 = (re.findall('[\d]+', gamescreen3.ids.pylya_3.text).pop())
                pylka = (re.findall('[\d]+', gamescreen3.ids.button1.text).pop())
                oldgora1 = (re.findall('[\d]+',gamescreen3.ids.gora_1.text).pop())
                oldgora2 = (re.findall('[\d]+',gamescreen3.ids.gora_2.text).pop())
                oldgora3 = (re.findall('[\d]+',gamescreen3.ids.gora_3.text).pop())
                vist_1_2 = (re.findall('[\d]+',gamescreen3.ids.vist_1_2.text).pop())
                vist_1_3 = (re.findall('[\d]+',gamescreen3.ids.vist_1_3.text).pop())
                vist_2_1 = (re.findall('[\d]+',gamescreen3.ids.vist_2_1.text).pop())
                vist_2_3 = (re.findall('[\d]+',gamescreen3.ids.vist_2_3.text).pop())
                vist_3_1 = (re.findall('[\d]+',gamescreen3.ids.vist_3_1.text).pop())
                vist_3_2 = (re.findall('[\d]+',gamescreen3.ids.vist_3_2.text).pop())
                fileload.write('game3\n')
                fileload.write(name1 + '\n')
                fileload.write(pylya1 + '\n')
                fileload.write(oldgora1 + '\n')
                fileload.write(vist_1_2 + '\n')
                fileload.write(vist_1_3 + '\n')
                fileload.write(name2 + '\n')
                fileload.write(pylya2 + '\n')
                fileload.write(oldgora2 + '\n')
                fileload.write(vist_2_1 + '\n')
                fileload.write(vist_2_3 + '\n')
                fileload.write(name3 + '\n')
                fileload.write(pylya3 + '\n')
                fileload.write(oldgora3 + '\n')
                fileload.write(vist_3_1 + '\n')
                fileload.write(vist_3_2 + '\n')
                fileload.close()
            else:
                fileload = open("load.txt", 'w')
                gamescreen4 = sm.get_screen("game4")
                name1 = gamescreen4.ids.label1.text
                name2 = gamescreen4.ids.label2.text
                name3 = gamescreen4.ids.label3.text
                name4 = gamescreen4.ids.label4.text
                pylya1 = (re.findall('[\d]+', gamescreen4.ids.pylya_1.text).pop())
                pylya2 = (re.findall('[\d]+', gamescreen4.ids.pylya_2.text).pop())
                pylya3 = (re.findall('[\d]+', gamescreen4.ids.pylya_3.text).pop())
                pylya4 = (re.findall('[\d]+', gamescreen4.ids.pylya_4.text).pop())
                pylka = (re.findall('[\d]+', gamescreen4.ids.button1.text).pop())
                oldgora1 = (re.findall('[\d]+',gamescreen4.ids.gora_1.text).pop())
                oldgora2 = (re.findall('[\d]+',gamescreen4.ids.gora_2.text).pop())
                oldgora3 = (re.findall('[\d]+',gamescreen4.ids.gora_3.text).pop())
                oldgora4 = (re.findall('[\d]+',gamescreen4.ids.gora_4.text).pop())
                vist_1_2 = (re.findall('[\d]+',gamescreen4.ids.vist_1_2.text).pop())
                vist_1_3 = (re.findall('[\d]+',gamescreen4.ids.vist_1_3.text).pop())
                vist_1_4 = (re.findall('[\d]+',gamescreen4.ids.vist_1_4.text).pop())
                vist_2_1 = (re.findall('[\d]+',gamescreen4.ids.vist_2_1.text).pop())
                vist_2_3 = (re.findall('[\d]+',gamescreen4.ids.vist_2_3.text).pop())
                vist_2_4 = (re.findall('[\d]+',gamescreen4.ids.vist_2_4.text).pop())
                vist_3_1 = (re.findall('[\d]+',gamescreen4.ids.vist_3_1.text).pop())
                vist_3_2 = (re.findall('[\d]+',gamescreen4.ids.vist_3_2.text).pop())
                vist_3_4 = (re.findall('[\d]+',gamescreen4.ids.vist_3_4.text).pop())
                vist_4_1 = (re.findall('[\d]+',gamescreen4.ids.vist_4_1.text).pop())
                vist_4_2 = (re.findall('[\d]+',gamescreen4.ids.vist_4_2.text).pop())
                vist_4_3 = (re.findall('[\d]+',gamescreen4.ids.vist_4_3.text).pop())
                fileload.write('game4\n')
                fileload.write(name1 + '\n')
                fileload.write(pylya1 + '\n')
                fileload.write(oldgora1 + '\n')
                fileload.write(vist_1_2 + '\n')
                fileload.write(vist_1_3 + '\n')
                fileload.write(vist_1_4 + '\n')
                fileload.write(name2 + '\n')
                fileload.write(pylya2 + '\n')
                fileload.write(oldgora2 + '\n')
                fileload.write(vist_2_1 + '\n')
                fileload.write(vist_2_3 + '\n')
                fileload.write(vist_2_4 + '\n')
                fileload.write(name3 + '\n')
                fileload.write(pylya3 + '\n')
                fileload.write(oldgora3 + '\n')
                fileload.write(vist_3_1 + '\n')
                fileload.write(vist_3_2 + '\n')
                fileload.write(vist_3_4 + '\n')
                fileload.write(name4 + '\n')
                fileload.write(pylya4 + '\n')
                fileload.write(oldgora4 + '\n')
                fileload.write(vist_4_1 + '\n')
                fileload.write(vist_4_2 + '\n')
                fileload.write(vist_4_3 + '\n')
                fileload.close()
            return False
        popup = MyPopup(title='Введите значение',
              auto_dismiss=False,size_hint=(.5, .2))
        popup.bind(on_dismiss=my_dismiss)
        popup.open()

    def update_pulya(self, instance):
        self.instance = instance
        def my_dismiss(instance):
            self.value = instance.ids.text1.text
            self.instance.text=self.value
            return False
        popup = MyPopup(title='Введите значение',
              auto_dismiss=False,size_hint=(.5, .2))
        popup.bind(on_dismiss=my_dismiss)
        popup.open()
        def on_pause(self):
            return True


if __name__=="__main__":
    if os.path.exists("mydatabase.db") == False:
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        cursor.execute(""" CREATE TABLE stats
                (numbers integer, first_player text, first_player_stat text,
                second_player text, second_player_stat text,
                third_player text, third_player_stat text,
                fourth_player text, fourth_player_stat text)
                """)
    MyApp().run()
