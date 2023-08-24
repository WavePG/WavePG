# Imports
from tkinter import *
import os
import sys
import configparser

config = configparser.ConfigParser()

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
label_1 = column_1['1n']
label_2 = column_2['2n']
label_3 = column_3['3n']
label_4 = column_4['4n']
label_5 = column_5['5n']
label_6 = column_6['6n']
label_7 = column_7['7n']
label_8 = column_8['8n']
label_9 = column_9['9n']
config_key = settings['verification_key']
config_title = settings['title']
config_rows = int(settings['rows'])
config_columns = int(settings['columns'])
config_theme = settings['theme']


theme, accent, a_theme, a_accent = '#282E33', '#FFF', '#006E62', '#FFF'
font = 'Arial'
current_theme = config_theme
a_sidebar, sidebar, scroll_theme = '#006E62', '#18191D', '#008080'
points = 0
show_cp = 0
cp_a_show, cp_current = 0, 0
title, ans, que = 'Null/Void', 'Null/Void', 'Null/Void' 
current_ver = '1.0.0'

def reset():
    global state_a1,  state_a3, state_a5, state_b1, state_b3, state_b5, state_c1, state_c3, state_c5, state_d1, state_d3, state_d5, state_e1, state_e3, state_e5, state_f1, state_f3, state_f5, state_g1, state_g3, state_g5, state_h1, state_h3, state_h5, state_i1, state_i3, state_i5, state_a2,  state_a4, state_b2, state_b4, state_c2, state_c4, state_d2, state_d4, state_e2, state_e4, state_f2, state_f4, state_g2, state_g4, state_h2, state_h4, state_i2, state_i4, points
    state_a1,  state_a3, state_a5, state_b1, state_b3, state_b5, state_c1, state_c3, state_c5, state_d1, state_d3, state_d5, state_e1, state_e3, state_e5, state_f1, state_f3, state_f5, state_g1, state_g3, state_g5, state_h1, state_h3, state_h5, state_i1, state_i3, state_i5 = accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent
    state_a2,  state_a4, state_b2, state_b4, state_c2, state_c4, state_d2, state_d4, state_e2, state_e4, state_f2, state_f4, state_g2, state_g4, state_h2, state_h4, state_i2, state_i4 = accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent, accent
    points = 0
    verify()

def about():  # About Jeopardy Player
    clear_frame()
    side_bar()
    Label(frame, text='Jeopardy Player\n', font=(font, 40), bg=theme,
          fg=a_accent).grid(row=0, column=0, sticky='NSEW')
    Label(frame, text=('Release '+current_ver+'''
\nA Python program that's for Jeopardy
\nMaker = Wave
\nMade on Thonny Python IDE with Python 3.11.3 + Tkinter 8.6.13
\nTested on GNU+Linux(Manjaro+Plasma 5)
\n©2023 TSUNAMI CO
\nProtected under the GNU Lesser
\nGeneral Public Licence (GNU LGPL) 3.0
\nDM for Source Code
\nBreath theme adapted from Manjaro KDE
    '''), font=(font, 20), bg=theme, fg=accent).grid(row=1, column=0, sticky='NSEW')
    
def question(): # Display Question
    clear_frame()
    side_bar()
    global title_color
#     if title[0] == '1':
#         title_color = '#0F0'
#     if title[0] == '3':
#         title_color = '#F70'
#     if title[0] == '5':
#         title_color = '#F0F'
    title_color = '#FFF'
                
    Label(frame, text=str(title), bg=theme, activebackground=a_theme,
                      fg=title_color, activeforeground=a_accent,  font=(font, 40)).grid(row=0, column=1, sticky='NSEW')
    Label(frame, text=str(que), bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent,  font=(font, 20)).grid(row=1, column=1, sticky='NSEW')
    if show_cp == 0:
        Button(frame, text='Reveal', width=50, command=reveal, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=(font, 40)).grid(row=2, column=1, sticky='NSEW')
    r.title('Jeopardy - '+title)

def reveal(): # Reveal Answer
    clear_frame()
    Label(frame, text=str(title), bg=theme, activebackground=a_theme,
                  fg=title_color, activeforeground=a_accent,  font=(font, 40)).grid(row=0, column=1, sticky='NSEW')
    Label(frame, text=str(que), bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent,  font=(font, 20)).grid(row=1, column=1, sticky='NSEW')
    Label(frame, text=str('\n'+ans), width=50, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=(font, 20)).grid(row=2, column=1, sticky='NSEW')

def main():  # Game
    clear_frame()
    d_bar()
    r.title('Jeopardy Player')
    def qa1():
        global  que, ans, title, state_a1
        state_a1 = '#F00'
        title = column_1['1n']+' - 100'
        que = column_1['1q1']
        ans = column_1['1a1']
        question()
    def qa2():
        global  que, ans, title, state_a2
        state_a2 = '#F00'
        title = column_1['1n']+' - 200'
        que = column_1['1q2']
        ans = column_1['1a2']
        question()
    def qa3():
        global  que, ans, title, state_a3
        state_a3 = '#F00'
        title = column_1['1n']+' - 300'
        que = column_1['1q3']
        ans = column_1['1a3']
        question()
    def qa4():
        global  que, ans, title, state_a4
        state_a4 = '#F00'
        title = column_1['1n']+' - 400'
        que = column_1['1q4']
        ans = column_1['1a4']
        question()
    def qa5():
        global  que, ans, title, state_a5
        state_a5 = '#F00'
        title = column_1['1n']+' - 500'
        que = column_1['1q5']
        ans = column_1['1a5']
        question()
    def qb1():
        global  que, ans, title, state_b1
        state_b1 = '#F00'
        title = column_2['2n']+' - 100'
        que = column_2['2q1']
        ans = column_2['2a1']
        question()
    def qb2():
        global  que, ans, title, state_b2
        state_b2 = '#F00'
        title = column_2['2n']+' - 200'
        que = column_2['2q2']
        ans = column_2['2a2']
        question()
    def qb3():
        global  que, ans, title, state_b3
        state_b3 = '#F00'
        title = column_2['2n']+' - 300'
        que = column_2['2q3']
        ans = column_2['2a3']
        question()
    def qb4():
        global  que, ans, title, state_b4
        state_b4 = '#F00'
        title = column_2['2n']+' - 400'
        que = column_2['2q4']
        ans = column_2['2a4']
        question()
    def qb5():
        global  que, ans, title, state_b5
        state_b5 = '#F00'
        title = column_2['2n']+' - 500'
        que = column_2['2q5']
        ans = column_2['2a5']
        question()
    def qc1():
        global  que, ans, title, state_c1
        state_c1 = '#F00'
        title = column_3['3n']+' - 100'
        que = column_3['3q1']
        ans = column_3['3a1']
        question()
    def qc2():
        global  que, ans, title, state_c2
        state_c2 = '#F00'
        title = column_3['3n']+' - 200'
        que = column_3['3q2']
        ans = column_3['3a2']
        question()
    def qc3():
        global  que, ans, title, state_c3
        state_c3 = '#F00'
        title = column_3['3n']+' - 300'
        que = column_3['3q3']
        ans = column_3['3a3']
        question()
    def qc4():
        global  que, ans, title, state_c4
        state_c4 = '#F00'
        title = column_3['3n']+' - 400'
        que = column_3['3q4']
        ans = column_3['3a4']
        question()
    def qc5():
        global  que, ans, title, state_c5
        state_c5 = '#F00'
        title = column_3['3n']+' - 500'
        que = column_3['3q5']
        ans = column_3['3a5']
        question()
    def qd1():
        global  que, ans, title, state_d1
        state_d1 = '#F00'
        title = column_4['4n']+' - 100'
        que = column_4['4q1']
        ans = column_4['4a1']
        question()
    def qd2():
        global  que, ans, title, state_d2
        state_d2 = '#F00'
        title = column_4['4n']+' - 200'
        que = column_4['4q2']
        ans = column_4['4a2']
        question()
    def qd3():
        global  que, ans, title, state_d3
        state_d3 = '#F00'
        title = column_4['4n']+' - 300'
        que = column_4['4q3']
        ans = column_4['4a3']
        question()
    def qd4():
        global  que, ans, title, state_d4
        state_d4 = '#F00'
        title = column_4['4n']+' - 400'
        que = column_4['4q4']
        ans = column_4['4a4']
        question()
    def qd5():
        global  que, ans, title, state_d5
        state_d5 = '#F00'
        title = column_4['4n']+' - 500'
        que = column_4['4q5']
        ans = column_4['4a5']
        question()
    def qe1():
        global  que, ans, title, state_e1
        state_e1 = '#F00'
        title = column_5['5n']+' - 100'
        que = column_5['5q1']
        ans = column_5['5a1']
        question()
    def qe2():
        global  que, ans, title, state_e2
        state_e2 = '#F00'
        title = column_5['5n']+' - 200'
        que = column_5['5q2']
        ans = column_5['5a2']
        question()
    def qe3():
        global  que, ans, title, state_e3
        state_e3 = '#F00'
        title = column_5['5n']+' - 300'
        que = column_5['5q3']
        ans = column_5['5a3']
        question()
    def qe4():
        global  que, ans, title, state_e4
        state_e4 = '#F00'
        title = column_5['5n']+' - 400'
        que = column_5['5q4']
        ans = column_5['5a4']
        question()
    def qe5():
        global  que, ans, title, state_e5
        state_e5 = '#F00'
        title = column_5['5n']+' - 500'
        que = column_5['5q5']
        ans = column_5['5a5']
        question()
    def qf1():
        global  que, ans, title, state_f1
        state_f1 = '#F00'
        title = column_6['6n']+' - 100'
        que = column_6['6q1']
        ans = column_6['6a1']
        question()
    def qf2():
        global  que, ans, title, state_f2
        state_f2 = '#F00'
        title = column_6['6n']+' - 200'
        que = column_6['6q2']
        ans = column_6['6a2']
        question()
    def qf3():
        global  que, ans, title, state_f3
        state_f3 = '#F00'
        title = column_6['6n']+' - 300'
        que = column_6['6q3']
        ans = column_6['6a3']
        question()
    def qf4():
        global  que, ans, title, state_f4
        state_f4 = '#F00'
        title = column_6['6n']+' - 400'
        que = column_6['6q4']
        ans = column_6['6a4']
        question()
    def qf5():
        global  que, ans, title, state_f5
        state_f5 = '#F00'
        title = column_6['6n']+' - 500'
        que = column_6['6q5']
        ans = column_6['6a5']
        question()
    def qg1():
        global  que, ans, title, state_g1
        state_g1 = '#F00'
        title = column_7['7n']+' - 100'
        que = column_7['7q1']
        ans = column_7['7a1']
        question()
    def qg2():
        global  que, ans, title, state_g2
        state_g2 = '#F00'
        title = column_7['7n']+' - 200'
        que = column_7['7q2']
        ans = column_7['7a2']
        question()
    def qg3():
        global  que, ans, title, state_g3
        state_g3 = '#F00'
        title = column_7['7n']+' - 300'
        que = column_7['7q3']
        ans = column_7['7a3']
        question()
    def qg4():
        global  que, ans, title, state_g4
        state_g4 = '#F00'
        title = column_7['7n']+' - 400'
        que = column_7['7q4']
        ans = column_7['7a4']
        question()
    def qg5():
        global  que, ans, title, state_g5
        state_g5 = '#F00'
        title = column_7['7n']+' - 500'
        que = column_7['7q5']
        ans = column_7['7a5']
        question()
    def qh1():
        global  que, ans, title, state_h1
        state_h1 = '#F00'
        title = column_8['8n']+' - 100'
        que = column_8['8q1']
        ans = column_8['8a1'] 
        question()
    def qh2():
        global  que, ans, title, state_h2
        state_h2 = '#F00'
        title = column_8['8n']+' - 200'
        que = column_8['8q2']
        ans = column_8['8a2']
        question()
    def qh3():
        global  que, ans, title, state_h3
        state_h3 = '#F00'
        title = column_8['8n']+' - 300'
        que = column_8['8q3']
        ans = column_8['8a3']
        question()
    def qh4():
        global  que, ans, title, state_h4
        state_h4 = '#F00'
        title = column_8['8n']+' - 400'
        que = column_8['8q4']
        ans = column_8['8a4']
        question()
    def qh5():
        global  que, ans, title, state_h5
        state_h5 = '#F00'
        title = column_8['8n']+' - 500'
        que = column_8['8q5']
        ans = column_8['8a5']
        question()
    def qi1():
        global  que, ans, title, state_i1
        state_i1 = '#F00'
        title = column_9['9n']+' - 100'
        que = column_9['9q1']
        ans = column_9['9a1']
        question()
    def qi2():
        global  que, ans, title, state_i2
        state_i2 = '#F00'
        title = column_9['9n']+' - 200'
        que = column_9['9q2']
        ans = column_9['9a2']
        question()
    def qi3():
        global  que, ans, title, state_i3
        state_i3 = '#F00'
        title = column_9['9n']+' - 300'
        que = column_9['9q3']
        ans = column_9['9a3']
        question()
    def qi4():
        global  que, ans, title, state_i4
        state_i4 = '#F00'
        title = column_9['9n']+' - 400'
        que = column_9['9q4']
        ans = column_9['9a4']
        question()
    def qi5():
        global  que, ans, title, state_i5
        state_i5 = '#F00'
        title = column_9['9n']+' - 500'
        que = column_9['9q5']
        ans = column_9['9a5']
        question()


    a1 =  Button(frame, text='100', width=8, height=9, command=qa1, bg=theme, activebackground=a_theme,
                      fg=state_a1, activeforeground=a_accent, font=font).grid(row=2, column=0, sticky='NSEW')
    a2 =  Button(frame, text='200', width=8, height=9, command=qa2, bg=theme, activebackground=a_theme,
                      fg=state_a2, activeforeground=a_accent, font=font).grid(row=3, column=0, sticky='NSEW')
    a3 =  Button(frame, text='300', width=8, height=9, command=qa3, bg=theme, activebackground=a_theme,
                      fg=state_a3, activeforeground=a_accent, font=font).grid(row=4, column=0, sticky='NSEW')
    b1 =  Button(frame, text='100', width=8, height=9, command=qb1, bg=theme, activebackground=a_theme,
                      fg=state_b1, activeforeground=a_accent, font=font).grid(row=2, column=1, sticky='NSEW')
    b2 =  Button(frame, text='200', width=8, height=9, command=qb2, bg=theme, activebackground=a_theme,
                      fg=state_b2, activeforeground=a_accent, font=font).grid(row=3, column=1, sticky='NSEW')
    b3 =  Button(frame, text='300', width=8, height=9, command=qb3, bg=theme, activebackground=a_theme,
                      fg=state_b3, activeforeground=a_accent, font=font).grid(row=4, column=1, sticky='NSEW')
    c1 =  Button(frame, text='100', width=8, height=9, command=qc1, bg=theme, activebackground=a_theme,
                      fg=state_c1, activeforeground=a_accent, font=font).grid(row=2, column=2, sticky='NSEW')
    c2 =  Button(frame, text='200', width=8, height=9, command=qc2, bg=theme, activebackground=a_theme,
                      fg=state_c2, activeforeground=a_accent, font=font).grid(row=3, column=2, sticky='NSEW')
    c3 =  Button(frame, text='300', width=8, height=9, command=qc3, bg=theme, activebackground=a_theme,
                      fg=state_c3, activeforeground=a_accent, font=font).grid(row=4, column=2, sticky='NSEW')
    d1 =  Button(frame, text='100', width=8, height=9, command=qd1, bg=theme, activebackground=a_theme,
                      fg=state_d1, activeforeground=a_accent, font=font).grid(row=2, column=3, sticky='NSEW')
    d2 =  Button(frame, text='200', width=8, height=9, command=qd2, bg=theme, activebackground=a_theme,
                      fg=state_d2, activeforeground=a_accent, font=font).grid(row=3, column=3, sticky='NSEW')
    d3 =  Button(frame, text='300', width=8, height=9, command=qd3, bg=theme, activebackground=a_theme,
                      fg=state_d3, activeforeground=a_accent, font=font).grid(row=4, column=3, sticky='NSEW')
    e1 =  Button(frame, text='100', width=8, height=9, command=qe1, bg=theme, activebackground=a_theme,
                      fg=state_e1, activeforeground=a_accent, font=font).grid(row=2, column=4, sticky='NSEW')
    e2 =  Button(frame, text='200', width=8, height=9, command=qe2, bg=theme, activebackground=a_theme,
                      fg=state_e2, activeforeground=a_accent, font=font).grid(row=3, column=4, sticky='NSEW')
    e3 =  Button(frame, text='300', width=8, height=9, command=qe3, bg=theme, activebackground=a_theme,
                      fg=state_e3, activeforeground=a_accent, font=font).grid(row=4, column=4, sticky='NSEW')
    if config_rows >= 3:
        if config_columns >= 6:
                f1 =  Button(frame, text='100', width=8, height=9, command=qf1, bg=theme, activebackground=a_theme,
                      fg=state_f1, activeforeground=a_accent, font=font).grid(row=2, column=5, sticky='NSEW')
                f2 =  Button(frame, text='200', width=8, height=9, command=qf2, bg=theme, activebackground=a_theme,
                      fg=state_f2, activeforeground=a_accent, font=font).grid(row=3, column=5, sticky='NSEW')
                f3 =  Button(frame, text='300', width=8, height=9, command=qf3, bg=theme, activebackground=a_theme,
                      fg=state_f3, activeforeground=a_accent, font=font).grid(row=4, column=5, sticky='NSEW')
        if config_columns >= 7:
                g1 =  Button(frame, text='100', width=8, height=9, command=qg1, bg=theme, activebackground=a_theme,
                      fg=state_g1, activeforeground=a_accent, font=font).grid(row=2, column=6, sticky='NSEW')
                g2 =  Button(frame, text='200', width=8, height=9, command=qg2, bg=theme, activebackground=a_theme,
                      fg=state_g2, activeforeground=a_accent, font=font).grid(row=3, column=6, sticky='NSEW')
                g3 =  Button(frame, text='300', width=8, height=9, command=qg3, bg=theme, activebackground=a_theme,
                      fg=state_g3, activeforeground=a_accent, font=font).grid(row=4, column=6, sticky='NSEW')
        if config_columns >= 8:
                h1 =  Button(frame, text='100', width=8, height=9, command=qh1, bg=theme, activebackground=a_theme,
                      fg=state_h1, activeforeground=a_accent, font=font).grid(row=2, column=7, sticky='NSEW')
                h2 =  Button(frame, text='200', width=8, height=9, command=qh2, bg=theme, activebackground=a_theme,
                      fg=state_h2, activeforeground=a_accent, font=font).grid(row=3, column=7, sticky='NSEW')
                h3 =  Button(frame, text='300', width=8, height=9, command=qh3, bg=theme, activebackground=a_theme,
                      fg=state_h3, activeforeground=a_accent, font=font).grid(row=4, column=7, sticky='NSEW')
        if config_columns >= 9:
                i1 =  Button(frame, text='100', width=8, height=9, command=qi1, bg=theme, activebackground=a_theme,
                      fg=state_i1, activeforeground=a_accent, font=font).grid(row=2, column=8, sticky='NSEW')
                i2 =  Button(frame, text='200', width=8, height=9, command=qi2, bg=theme, activebackground=a_theme,
                      fg=state_i2, activeforeground=a_accent, font=font).grid(row=3, column=8, sticky='NSEW')
                i3 =  Button(frame, text='300', width=8, height=9, command=qi3, bg=theme, activebackground=a_theme,
                      fg=state_i3, activeforeground=a_accent, font=font).grid(row=4, column=8, sticky='NSEW')
    if config_rows == 5:
        if config_columns >= 1:
                a4 =  Button(frame, text='400', width=8, height=9, command=qa4, bg=theme, activebackground=a_theme,
                      fg=state_a4, activeforeground=a_accent, font=font).grid(row=5, column=0, sticky='NSEW')
                a5 =  Button(frame, text='500', width=8, height=9, command=qa5, bg=theme, activebackground=a_theme,
                      fg=state_a5, activeforeground=a_accent, font=font).grid(row=6, column=0, sticky='NSEW')
        if config_columns >= 2:
                b4 =  Button(frame, text='400', width=8, height=9, command=qb4, bg=theme, activebackground=a_theme,
                      fg=state_b4, activeforeground=a_accent, font=font).grid(row=5, column=1, sticky='NSEW')
                b5 =  Button(frame, text='500', width=8, height=9, command=qb5, bg=theme, activebackground=a_theme,
                      fg=state_b5, activeforeground=a_accent, font=font).grid(row=6, column=1, sticky='NSEW')
        if config_columns >= 3:
                c4 =  Button(frame, text='400', width=8, height=9, command=qc4, bg=theme, activebackground=a_theme,
                      fg=state_c4, activeforeground=a_accent, font=font).grid(row=5, column=2, sticky='NSEW')
                c5 =  Button(frame, text='500', width=8, height=9, command=qc5, bg=theme, activebackground=a_theme,
                      fg=state_c5, activeforeground=a_accent, font=font).grid(row=6, column=2, sticky='NSEW')
        if config_columns >= 4:
                d4 =  Button(frame, text='400', width=8, height=9, command=qd4, bg=theme, activebackground=a_theme,
                      fg=state_d4, activeforeground=a_accent, font=font).grid(row=5, column=3, sticky='NSEW')
                d5 =  Button(frame, text='500', width=8, height=9, command=qd5, bg=theme, activebackground=a_theme,
                      fg=state_d5, activeforeground=a_accent, font=font).grid(row=6, column=3, sticky='NSEW')
        if config_columns >= 5:
                e4 =  Button(frame, text='400', width=8, height=9, command=qe4, bg=theme, activebackground=a_theme,
                      fg=state_e4, activeforeground=a_accent, font=font).grid(row=5, column=4, sticky='NSEW')
                e5 =  Button(frame, text='500', width=8, height=9, command=qe5, bg=theme, activebackground=a_theme,
                      fg=state_e5, activeforeground=a_accent, font=font).grid(row=6, column=4, sticky='NSEW')
        if config_columns >= 6:
                f4 =  Button(frame, text='400', width=8, height=9, command=qf4, bg=theme, activebackground=a_theme,
                      fg=state_f4, activeforeground=a_accent, font=font).grid(row=5, column=5, sticky='NSEW')
                f5 =  Button(frame, text='500', width=8, height=9, command=qf5, bg=theme, activebackground=a_theme,
                      fg=state_f5, activeforeground=a_accent, font=font).grid(row=6, column=5, sticky='NSEW')
        if config_columns >= 7:
                g4 =  Button(frame, text='400', width=8, height=9, command=qg4, bg=theme, activebackground=a_theme,
                      fg=state_g4, activeforeground=a_accent, font=font).grid(row=5, column=6, sticky='NSEW')
                g5 =  Button(frame, text='500', width=8, height=9, command=qg5, bg=theme, activebackground=a_theme,
                      fg=state_g5, activeforeground=a_accent, font=font).grid(row=6, column=6, sticky='NSEW')
        if config_columns >= 8:
                h4 =  Button(frame, text='400', width=8, height=9, command=qh4, bg=theme, activebackground=a_theme,
                      fg=state_h4, activeforeground=a_accent, font=font).grid(row=5, column=7, sticky='NSEW')
                h5 =  Button(frame, text='500', width=8, height=9, command=qh5, bg=theme, activebackground=a_theme,
                      fg=state_h5, activeforeground=a_accent, font=font).grid(row=6, column=7, sticky='NSEW')
        if config_columns >= 9:
                i4 =  Button(frame, text='400', width=8, height=9, command=qi4, bg=theme, activebackground=a_theme,
                      fg=state_i4, activeforeground=a_accent, font=font).grid(row=5, column=8, sticky='NSEW')
                i5 =  Button(frame, text='500', width=8, height=9, command=qi5, bg=theme, activebackground=a_theme,
                      fg=state_i5, activeforeground=a_accent, font=font).grid(row=6, column=8, sticky='NSEW')








    Label(frame, text=label_1, bg=theme, activebackground=a_theme,
          fg=accent, activeforeground=a_accent,  font=(font, 10)).grid(row=1, column=0, sticky='NSEW')
    Label(frame, text=label_2, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent,  font=(font, 10)).grid(row=1, column=1, sticky='NSEW')
    Label(frame, text=label_3, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent,  font=(font, 10)).grid(row=1, column=2, sticky='NSEW')
    Label(frame, text=label_4, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent,  font=(font, 10)).grid(row=1, column=3, sticky='NSEW')
    Label(frame, text=label_5, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent,  font=(font, 10)).grid(row=1, column=4, sticky='NSEW')
    if config_rows >= 3:
        if config_columns >= 6:
            Label(frame, text=label_6, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent,  font=(font, 10)).grid(row=1, column=5, sticky='NSEW')
        if config_columns >= 7:
            Label(frame, text=label_7, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent,  font=(font, 10)).grid(row=1, column=6, sticky='NSEW')
        if config_columns >= 8:
            Label(frame, text=label_8, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent,  font=(font, 10)).grid(row=1, column=7, sticky='NSEW')
        if config_columns >= 9:
            Label(frame, text=label_9, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent,  font=(font, 10)).grid(row=1, column=8, sticky='NSEW')


def player_settings(event=None): # Settings
    clear_frame()
    side_bar()
    def save_settings():
        r.config(bg=theme)
        bar.config(bg=theme)
        frame.config(bg=theme)
        menu.config(bg=theme, activebackground=a_theme,
                fg=accent, activeforeground=a_accent, font=font)
        filemenu.config(bg=theme, activebackground=a_theme,
                    fg=accent, activeforeground=a_accent, font=font)
        helpmenu.config(bg=theme, activebackground=a_theme,
                    fg=accent, activeforeground=a_accent, font=font)
        side_bar()
    def themes(event=None):
        clear_frame()
        def dark_theme():
            global theme, accent, a_theme, a_accent, sidebar, a_sidebar, scroll_theme, current_theme
            current_theme = 'Dark'
            theme = '#161616'
            accent = '#FFF'
            a_theme = '#FE9700'
            a_accent = '#FFF'
            sidebar = '#101010'
            a_sidebar = '#F70'
            scroll_theme = '#F70'
            save_settings()
            Button(frame, text='<', width=1, command=player_settings, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent, font=font).grid(row=0, column=0, sticky='NSEW')
            Label(frame, text='Choose a Theme:         ', font=font,
                  bg=theme, fg=accent).grid(row=0, column=1, ipadx=325, sticky='NSEW')
            Label(frame, text=('Current Theme: '+current_theme+' Theme'), font=font,
                  bg=theme, fg=accent).grid(row=1, column=0, columnspan=2, sticky='NSEW')

        def light_theme():
            global theme, accent, a_theme, a_accent, sidebar, a_sidebar, scroll_theme, current_theme
            current_theme = 'Light'
            theme = '#F7F9FC'
            accent = '#000'
            a_theme = '#C2E7FF'
            a_accent = '#000'
            sidebar = '#EDF2FC'
            a_sidebar = '#00A4FD'
            scroll_theme = '#C2E7FF'
            save_settings()
            Button(frame, text='<', width=1, command=player_settings, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent, font=font).grid(row=0, column=0, sticky='NSEW')
            Label(frame, text='Choose a Theme:         ', font=font,
                  bg=theme, fg=accent).grid(row=0, column=1, ipadx=325, sticky='NSEW')
            Label(frame, text=('Current Theme: '+current_theme+' Theme'), font=font,
                  bg=theme, fg=accent).grid(row=1, column=0, columnspan=2, sticky='NSEW')

        def terminal_theme():
            global theme, accent, a_theme, a_accent, sidebar, a_sidebar, scroll_theme, current_theme
            current_theme = 'Terminal'
            theme = '#101010'
            accent = '#0F0'
            a_theme = '#2B2B2B'
            a_accent = '#F0F'
            sidebar = '#101010'
            a_sidebar = '#0F0'
            scroll_theme = '#F0F'
            save_settings()
            Button(frame, text='<', width=1, command=player_settings, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent, font=font).grid(row=0, column=0, sticky='NSEW')
            Label(frame, text='Choose a Theme:         ', font=font,
                  bg=theme, fg=accent).grid(row=0, column=1, ipadx=325, sticky='NSEW')
            Label(frame, text=('Current Theme: '+current_theme+' Theme'), font=font,
                  bg=theme, fg=accent).grid(row=1, column=0, columnspan=2, sticky='NSEW')

        def blue_theme():
            global theme, accent, a_theme, a_accent, sidebar, a_sidebar, scroll_theme, current_theme
            current_theme = 'Blue'
            theme = '#013E4B'
            accent = '#0094B4'
            a_theme = '#006378'
            a_accent = '#00A4FD'
            sidebar = '#268E9E'
            a_sidebar = '#006378'
            scroll_theme = '#00A4FD'
            save_settings()
            Button(frame, text='<', width=1, command=player_settings, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent, font=font).grid(row=0, column=0, sticky='NSEW')
            Label(frame, text='Choose a Theme:         ', font=font,
                  bg=theme, fg=accent).grid(row=0, column=1, ipadx=325, sticky='NSEW')
            Label(frame, text=('Current Theme: '+current_theme+' Theme'), font=font,
                  bg=theme, fg=accent).grid(row=1, column=0, columnspan=2, sticky='NSEW')

        def breath_theme():
            global theme, accent, a_theme, a_accent, sidebar, a_sidebar, scroll_theme, current_theme
            current_theme = 'Breath'
            theme = '#282E33'
            accent = '#FFF'
            a_theme = '#006E62'
            a_accent = '#FFF'
            sidebar = '#18191D'
            a_sidebar = '#006E62'
            scroll_theme = '#008080'
            save_settings()
            Button(frame, text='<', width=1, command=player_settings, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent, font=font).grid(row=0, column=0, sticky='NSEW')
            Label(frame, text='Choose a Theme:         ', font=font,
                  bg=theme, fg=accent).grid(row=0, column=1, ipadx=325, sticky='NSEW')
            Label(frame, text=('Current Theme: '+current_theme+' Theme'), font=font,
                  bg=theme, fg=accent).grid(row=1, column=0, columnspan=2, sticky='NSEW')

        Button(frame, text='<', width=1, command=player_settings, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent, font=font).grid(row=0, column=0, sticky='NSEW')
        Label(frame, text='Choose a Theme:         ', font=font,
              bg=theme, fg=accent).grid(row=0, column=1, ipadx=325, sticky='NSEW')
        Label(frame, text=('Current Theme: '+current_theme+' Theme'), font=font,
              bg=theme, fg=accent).grid(row=1, column=0, columnspan=2, sticky='NSEW')
        Button(frame, text='Dark Theme', width=90, command=dark_theme, bg='#161616', activebackground='#FE9700',
                  fg='#FFF', activeforeground='#FFF', font=font).grid(row=2, column=0, columnspan=2, sticky='NSEW')
        Button(frame, text='Light Theme', command=light_theme, bg='#F7F9FC', activebackground='#C2E7FF',
                  fg='#000', activeforeground='#000', font=font).grid(row=3, column=0, columnspan=2, sticky='NSEW')
        Button(frame, text='Terminal Theme', command=terminal_theme, bg='#101010', activebackground='#2B2B2B',
                  fg='#0F0', activeforeground='#F0F', font=font).grid(row=4, column=0, columnspan=2, sticky='NSEW')
        Button(frame, text='Blue Theme', command=blue_theme, bg='#013E4B', activebackground='#006378',
                  fg='#0094B4', activeforeground='#00A4FD', font=font).grid(row=5, column=0, columnspan=2, sticky='NSEW')
        Button(frame, text='Breath Theme', command=breath_theme, bg='#282E33', activebackground='#006E62',
                  fg='#FFF', activeforeground='#FFF', font=font).grid(row=6, column=0, columnspan=2, sticky='NSEW')
        r.bind('<Escape>', settings)

    def fonts():
        clear_frame()

        def arial_font():
            global font
            font = 'Arial'
            save_settings()
            Button(frame, text='<', width=1, command=player_settings, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent, font=font).grid(row=0, column=0, sticky='NSEW')
            Label(frame, text='Choose a font:             ', font=font,
                  bg=theme, fg=accent).grid(row=0, column=1, ipadx=300, sticky='NSEW')
            Label(frame, text=('Current Font: '+font), font=font,
                  bg=theme, fg=accent).grid(row=1, column=0, columnspan=2, sticky='NSEW')
            Label(frame, text='*Some fonts may break UI', font=font,
                  bg=theme, fg=accent).grid(row=7, column=0, columnspan=2, sticky='NSEW')
            Label(frame, text='*Some fonts may need to be downloaded', font=font,
                  bg=theme, fg=accent).grid(row=8, column=0, columnspan=2, sticky='NSEW')

        def times_font():
            global font
            font = 'Times'
            save_settings()
            Button(frame, text='<', width=1, command=player_settings, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent, font=font).grid(row=0, column=0, sticky='NSEW')
            Label(frame, text='Choose a font:             ', font=font,
                  bg=theme, fg=accent).grid(row=0, column=1, ipadx=300, sticky='NSEW')
            Label(frame, text=('Current Font: '+font), font=font,
                  bg=theme, fg=accent).grid(row=1, column=0, columnspan=2, sticky='NSEW')
            Label(frame, text='*Some fonts may break UI', font=font,
                  bg=theme, fg=accent).grid(row=7, column=0, columnspan=2, sticky='NSEW')
            Label(frame, text='*Some fonts may need to be downloaded', font=font,
                  bg=theme, fg=accent).grid(row=8, column=0, columnspan=2, sticky='NSEW')

        def ubuntu_font():
            global font
            font = 'Ubuntu'
            save_settings()
            Button(frame, text='<', width=1, command=player_settings, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent, font=font).grid(row=0, column=0, sticky='NSEW')
            Label(frame, text='Choose a font:             ', font=font,
                  bg=theme, fg=accent).grid(row=0, column=1, ipadx=300, sticky='NSEW')
            Label(frame, text=('Current Font: '+font), font=font,
                  bg=theme, fg=accent).grid(row=1, column=0, columnspan=2, sticky='NSEW')
            Label(frame, text='*Some fonts may break UI', font=font,
                  bg=theme, fg=accent).grid(row=7, column=0, columnspan=2, sticky='NSEW')

        Button(frame, text='<', width=1, command=player_settings, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent, font=font).grid(row=0, column=0, sticky='NSEW')
        Label(frame, text='Choose a font:             ', font=font,
                  bg=theme, fg=accent).grid(row=0, column=1, ipadx=325, sticky='NSEW')
        Label(frame, text=('Current Font: '+font), font=font,
                  bg=theme, fg=accent).grid(row=1, column=0, columnspan=2, sticky='NSEW')
        Button(frame, text='Arial Font', width=90, command=arial_font, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent, font='Arial').grid(row=2, column=0, columnspan=2, sticky='NSEW')
        Button(frame, text='Times Font*', command=times_font, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent, font='Times').grid(row=3, column=0, columnspan=2, sticky='NSEW')
        Button(frame, text='Ubuntu Font*', command=ubuntu_font, bg=theme, activebackground=a_theme,
                  fg=accent, activeforeground=a_accent, font='Ubuntu').grid(row=4, column=0, columnspan=2, sticky='NSEW')
        Label(frame, text='*Some fonts may break UI', font=font,
                  bg=theme, fg=accent).grid(row=7, column=0, columnspan=2, sticky='NSEW')
        Label(frame, text='*Some fonts may need to be downloaded', font=font,
                  bg=theme, fg=accent).grid(row=8, column=0, columnspan=2, sticky='NSEW')
        r.bind('<Escape>', settings)
        
    Button(frame, text='Themes', command=themes, bg=theme, activebackground=a_theme,
              fg=accent, activeforeground=a_accent, font=font).grid(row=1, column=0, sticky='NSEW')
    Button(frame, text='Fonts', command=fonts, bg=theme, activebackground=a_theme,
              fg=accent, activeforeground=a_accent, font=font).grid(row=2, column=0, sticky='NSEW')
    Label(frame, text='\nReset', font=font,
                  bg=theme, fg=accent).grid(row=3, column=0, sticky='NSEW')
    Button(frame, text='Reset Picked Questions', command=reset, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=font).grid(row=4, column=0, sticky='NSEW')

def changelog():  # Changelog
    clear_frame()
    side_bar()
    log = Text(frame, height=100)
    log.pack(anchor='sw',side=LEFT, ipadx=30)
    logbar = Scrollbar(frame)
    logbar.pack(anchor='se',side=RIGHT, fill=BOTH)
    log.config(fg=a_accent)
    log.config(insertbackground=a_sidebar, selectbackground=scroll_theme)
    logbar.config(command=log.yview, bg=sidebar, activebackground=scroll_theme)
    log.config(font=(font, 20), bg=sidebar, yscrollcommand=logbar.set)
    change_path = resource_path('change.txt')
    with open(change_path, 'r') as f:
        log.insert(INSERT, ('Current Ver:  '+current_ver+'\n'+f.read()))

def clear_frame():  # Clear part of the window
    for widgets in frame.winfo_children():
        widgets.destroy()

def homepage():  # Reload Main Window
    clear_frame()
    
def side_bar():
    Button(bar, command=verify, text='<',
              bg=sidebar, activebackground=a_sidebar,
              fg=accent, activeforeground=a_accent,
              font=font, height=50, width=10).grid(row=0, column=0, sticky='NSEW')
        
def d_bar():
    for widgets in bar.winfo_children():
        widgets.destroy()

def end():
    clear_frame()
    Label(frame, text='Game Finished!', font=(font, 60),
              bg=theme, fg=accent).grid(row=6, column=0, sticky='NSEW')
    
def verify():
    if config_key[0:4] == (config_title[0:2]+str(config_rows)+str(config_columns)): # Decode for *reasons*
        main()
    else:
        clear_frame()
        Label(frame, text='Game has been tampered with outside of the creator!\nPlease reload the general settings!', font=(font, 60),
              bg=theme, fg=accent).grid(row=6, column=0, sticky='NSEW')
        d_bar()

def control_panel():
    global  show_cp, cp_current
    cp_current = 0
    if show_cp == 0:
        show_cp = 1
        cp = Toplevel()
        cp.title('Control Panel')
        cp.geometry('720x720')
        cp.config(bg=theme)
        cp_frame = Frame(cp, bg=theme)
        cp_frame.pack(side="bottom", expand=True)
        tabs = Frame(cp, bg=theme)
        tabs.pack(side="top", expand=False, fill='x')
        def clear_cp():  # Clear part of the window
            for widgets in cp_frame.winfo_children():
                widgets.destroy()
        def cp_points():
            clear_cp()
            global cp_current
            cp_current = 4
            def answer_correct():
                global points, title
                if title[0] == '1':
                    points = points + 100
                if title[0] == '3':
                    points = points + 300
                if title[0] == '5':
                    points = points + 500
                cp_points()
            def p10():
                global points
                points = points + 10
                cp_points()
            def p50():
                global points
                points = points + 50
                cp_points()
            def p100():
                global points
                points = points + 100
                cp_points()
            def n10():
                global points
                points = points - 10
                cp_points()
            def n50():
                global points
                points = points - 50
                cp_points()
            def n100():
                global points
                points = points - 100
                cp_points()
            Button(cp_frame, text='Full Points\nFor Answer', command=answer_correct, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=font, height=7, width=76).grid(row=0, column=0, columnspan=2, sticky='NSEW')
            Button(cp_frame, text='+10 Points', command=p10, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=font, height=7).grid(row=1, column=0, sticky='NSEW')
            Button(cp_frame, text='+50 Points', command=p50, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=font, height=7).grid(row=2, column=0, sticky='NSEW')
            Button(cp_frame, text='+100 Points', command=p100, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=font, height=7).grid(row=3, column=0, sticky='NSEW')
            Button(cp_frame, text='-10 Points', command=n10, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=font, height=7).grid(row=1, column=1, sticky='NSEW')
            Button(cp_frame, text='-50 Points', command=n50, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=font, height=7).grid(row=2, column=1, sticky='NSEW')
            Button(cp_frame, text='-100 Points', command=n100, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=font, height=7).grid(row=3, column=1, sticky='NSEW')
            Button(tabs, text=('Points: '+str(points)), command=cp_points, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=font).grid(row=0, column=3, sticky='NSEW')
        def controls():
            clear_cp()
            global cp_current
            cp_current = 1
            Button(cp_frame, text='Reveal Answer', command=reveal, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=font, width=76, height=9).grid(row=0, column=0, sticky='NSEW')
            Button(cp_frame, text='Home', command=verify, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=font, height=9).grid(row=2, column=0, sticky='NSEW')
            Button(cp_frame, text='CP Answers', command=cp_ans, bg=theme, activebackground=a_theme,
                              fg=accent, activeforeground=a_accent, font=font, height=9).grid(row=3, column=0, sticky='NSEW')
        def cp_settings():
            clear_cp()
            global cp_current
            cp_current = 2
            def reset_points(): # Reset Points
                global points
                points = 0
                cp_points()
            Label(cp_frame, text='Reset', font=font,
                          bg=theme, fg=accent, height=3).grid(row=0, column=0, sticky='NSEW')
            Button(cp_frame, text='Reset Picked Questions', command=reset, bg=theme, activebackground=a_theme,
                              fg=accent, activeforeground=a_accent, font=font, height=4).grid(row=1, column=0, sticky='NSEW')
            Button(cp_frame, text='Reset Points', command=reset_points, bg=theme, activebackground=a_theme,
                          fg=accent, activeforeground=a_accent, font=font, height=4).grid(row=2, column=0, sticky='NSEW')

        def cp_ans(): # Answers in CP
            global cp_a_show, cp_current
            cp_current = 3
            if cp_a_show == 0:
                cp_a_show = 1
            else:
                cp_a_show = 0
            clear_cp()
            Button(cp_frame, text='Reveal Answer', command=reveal, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=font, width=76).grid(row=0, column=0, sticky='NSEW')
            Label(cp_frame, text=(str(title)), font=font,
                  bg=theme, fg=accent, width = 60).grid(row=1, column=0, sticky='NSEW')
            Label(cp_frame, text=(str(ans)), font=font,
                      bg=theme, fg=accent).grid(row=2, column=0, sticky='NSEW')
        Button(tabs, text='Control', command=controls, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=font).grid(row=0, column=0, sticky='NSEW')
        Button(tabs, text='Settings', command=cp_settings, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=font).grid(row=0, column=1, sticky='NSEW')
        Button(tabs, text=('Points: '+str(points)), command=cp_points, bg=theme, activebackground=a_theme,
                      fg=accent, activeforeground=a_accent, font=font).grid(row=0, column=3, sticky='NSEW')
        controls()
    else:
        show_cp = 0

# Main Window
r = Tk()
r.geometry('1920x1080')
menu = Menu(r)
r.config(bg=theme, menu=menu)
r.title('Jeopardy Player')

frame = Frame(r, bg=theme)
frame.pack(side="right", expand=True)
bar = Frame(r, bg=theme)
bar.pack(side="left", expand=False, fill='x')

# Menu
filemenu = Menu(menu)
menu.config(bg=theme, activebackground=a_theme,
            fg=accent, activeforeground=a_accent, font=font)
menu.add_cascade(label='File', menu=filemenu, command=r.destroy)
filemenu.config(bg=theme, activebackground=a_theme,
                fg=accent, activeforeground=a_accent, font=font)
filemenu.add_command(label='Show Control Panel', command=control_panel)
filemenu.add_command(label='Exit', command=r.destroy)

helpmenu = Menu(menu)
helpmenu.config(bg=theme, activebackground=a_theme,
                fg=accent, activeforeground=a_accent, font=font)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Home', command=verify)
helpmenu.add_command(label='Settings', command=player_settings)
helpmenu.add_command(label='Changelog', command=changelog)
helpmenu.add_command(label='About', command=about)


reset()

r.mainloop()


