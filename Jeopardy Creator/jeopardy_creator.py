from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import  uic
import configparser
import os
import random as rand
import messagebox


config = configparser.ConfigParser()

#Key NameLetter1,NameLetter2+1LetterForward,Rows,Columns,Theme#,Slot#*(3/5/8)
# Default,3,5,Breath,Slot1
# Df35003, Df35005, Df35008
# 1: 03 05 08
# 2: 06 10 16
# 3: 09 15 24

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath('.')

    return os.path.join(base_path, relative_path)

edit = configparser.ConfigParser()
config_path = resource_path('slot_1.ini')
edit.read(config_path)
settings = edit["settings"]
column_1 = edit["c1"]
column_2 = edit["c2"]
column_3 = edit["c3"]
column_4 = edit["c4"]
column_5 = edit["c5"]
column_6 = edit["c6"]
column_7 = edit["c7"]
column_8 = edit["c8"]
column_9 = edit["c9"]
config_key = settings['verification_key']
config_title = settings['title']
config_columns = settings['rows']
config_rows = settings['columns']
config_theme = settings['theme']


class JC_UI(QMainWindow):
    
    def __init__(self):
        super(JC_UI, self).__init__()
        uic.loadUi('creator.ui', self)
        self.show()
        self.general_apply.clicked.connect(self.apply_general_settings)
        self.topics_apply.clicked.connect(self.apply_topic_names)
        self.reset_button.clicked.connect(self.reset)
        self.generate_button.clicked.connect(self.generate)
        self.get_current.clicked.connect(self.getQA)
        self.clear_current.clicked.connect(self.clear)
        self.label_24.setText(config_title)
        self.label_25.setText(config_rows)
        self.label_26.setText(config_columns)
        self.label_27.setText(config_theme)
    
    def getQA(self):
        self.question_input.clear()
        self.answer_input.clear()
        current_row = self.choose_row.currentIndex()+1
        current_column = self.choose_column.currentIndex()+1
        que = str(current_column)+'q'+str(current_row)
        ans = str(current_column)+'a'+str(current_row)
        if current_column == 1:
            currentQ = column_1[que]
            currentA = column_1[ans]
        if current_column == 2:
            currentQ = column_2[que]
            currentA = column_2[ans]
        if current_column == 3:
            currentQ = column_3[que]
            currentA = column_3[ans]
        if current_column == 4:
            currentQ = column_4[que]
            currentA = column_4[ans]
        if current_column == 5:
            currentQ = column_5[que]
            currentA = column_5[ans]
        if current_column == 6:
            currentQ = column_6[que]
            currentA = column_6[ans]
        if current_column == 7:
            currentQ = column_7[que]
            currentA = column_7[ans]
        if current_column == 8:
            currentQ = column_8[que]
            currentA = column_8[ans]
        if current_column == 9: 
            currentQ = column_9[que]
            currentA = column_9[ans]
        if currentQ == '' or currentQ == '#':
            self.current_que.setText('There is no question')
        else:
            self.question_input.append(currentQ)
        if currentA == '' or currentA == '#':
            self.current_ans.setText('There is no answer')
        else:
            self.answer_input.append(currentA)        
    
    def clear(self):
        self.question_input.clear()
        self.answer_input.clear()
        self.current_que.setText('Question was cleared')
        self.current_ans.setText('Answer was cleared')
        current_row = self.choose_row.currentIndex()+1
        current_column = self.choose_column.currentIndex()+1
        que = str(current_column)+'q'+str(current_row)
        ans = str(current_column)+'a'+str(current_row)
        if current_column == 1:
            column_1[que] = '#'
            column_1[ans] = '#'
        if current_column == 2:
            column_2[que] = '#'
            column_2[ans] = '#'
        if current_column == 3:
            column_3[que] = '#'
            column_3[ans] = '#'
        if current_column == 4:
            column_4[que] = '#'
            column_4[ans] = '#'
        if current_column == 5:
            column_5[que] = '#'
            column_5[ans] = '#'
        if current_column == 6:
            column_6[que] = '#'
            column_6[ans] = '#'
        if current_column == 7:
            column_7[que] = '#'
            column_7[ans] = '#'
        if current_column == 8:
            column_8[que] = '#'
            column_8[ans] = '#'
        if current_column == 9: 
            column_9[que] = '#'
            column_9[ans] = '#'
        with open('slot_1.ini', 'w',) as configfile:
            edit.write(configfile)
    
    def reset(self):
        settings['verification_key'] = 'Nu3501'
        settings['title'] = 'Placeholder'
        settings['rows'] = '3'
        settings['columns'] = '5'
        settings['theme'] = '0'
        with open('slot_1.ini', 'w',) as configfile:
            edit.write(configfile)
        self.label_24.setText(config_title)
        self.label_25.setText(config_rows)
        self.label_26.setText(config_columns)
        self.label_27.setText(config_theme)
        
    def apply_topic_names(self):
        colget = self.topic_number.value()
        top_name = self.topic_name.text()
        print(colget)
        if colget == 1:
            column_1['1n'] = top_name
        if colget == 2:
            column_2['2n'] = top_name
        if colget == 3:
            column_3['3n'] = top_name
        if colget == 4:
            column_4['4n'] = top_name
        if colget == 5:
            column_5['5n'] = top_name
        if colget == 6:
            column_6['6n'] = top_name
        if colget == 7:
            column_7['7n'] = top_name
        if colget == 8:
            column_8['8n'] = top_name
        if colget == 9: 
            column_9['9n'] = top_name
        with open('slot_1.ini', 'w',) as configfile:
            edit.write(configfile)
        self.topic_name.setText('')
           
    def apply_general_settings(self): # apply general settings
        name = self.game_name.text()
        rows = str(self.row_settings.value())
        columns = str(self.column_settings.value())
        theme = str(self.theme_select.currentText())
        if name != '':
            rand_int = rand.randint(0,2)
            if rand_int == 0:
                rand_int = 3
            if rand_int == 1:
                rand_int = 5
            if rand_int == 2:
                rand_int = 8
            key = (name[0:2]+rows+columns+str(self.theme_select.currentIndex())+str(rand_int))
            settings['verification_key'] = key # Encode for *reasons*
            settings['title'] = name
            settings['rows'] = rows
            settings['columns'] = columns
            settings['theme'] = theme
            with open('slot_1.ini', 'w',) as configfile:
                edit.write(configfile)
        else:
            messagebox.showerror('Jeopardy Creator Applier', 'ERR: tiNULL\nCould not apply changes\ndue to lack of a title!')

    
    def generate(self):
        q_slot = str(self.choose_column.currentIndex()+1)+('q')+str(self.choose_row.currentIndex()+1)
        a_slot = str(self.choose_column.currentIndex()+1)+('a')+str(self.choose_row.currentIndex()+1)
        c_slot = self.choose_column.currentIndex()+1
        if self.question_input.toPlainText() == '':
            que = '#'
        else:
            que = self.question_input.toPlainText()
        if self.answer_input.toPlainText() == '':
            ans = '#'
        else:
            ans = self.answer_input.toPlainText()
        if c_slot == 1:
            column_1[q_slot] = que
            column_1[a_slot] = ans
        if c_slot == 2:
            column_2[q_slot] = que
            column_2[a_slot] = ans
        if c_slot == 3:
            column_3[q_slot] = que
            column_3[a_slot] = ans
        if c_slot == 4:
            column_4[q_slot] = que
            column_4[a_slot] = ans
        if c_slot == 5:
            column_5[q_slot] = que
            column_5[a_slot] = ans
        if c_slot == 6:
            column_6[q_slot] = que
            column_6[a_slot] = ans
        if c_slot == 7:
            column_7[q_slot] = que
            column_7[a_slot] = ans
        if c_slot == 8:
            column_8[q_slot] = que
            column_8[a_slot] = ans
        if c_slot == 9:
            column_9[q_slot] = que
            column_9[a_slot] = ans
        with open('slot_1.ini', 'w',) as configfile:
            edit.write(configfile)
        self.current_que.setText('New question was saved')
        self.current_ans.setText('New answer was saved')


def main():
    app = QApplication([])
    window = JC_UI()
    app.exec_()


if __name__ == '__main__':
    main()
