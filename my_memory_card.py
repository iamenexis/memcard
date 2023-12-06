#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QPushButton, QHBoxLayout,
    QVBoxLayout, QLabel,
    QMessageBox, QRadioButton,
    QGroupBox, QButtonGroup
)

from random import shuffle, randint


class Questions():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Questions('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(Questions('Какого цвета нет на флаге России?', 'Зеленый', 'Красный', 'Белый', 'Синий'))
questions_list.append(Questions('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
questions_list.append(Questions('В чем секрет кота Бориса?', 'Он Борис', 'Не знаю', 'Корм', 'что'))
questions_list.append(Questions('Большое красное пятно на Юпитере, что это?', 'Сильный Шторм', 'Вулкан', 'буря', 'кратер'))
questions_list.append(Questions('Какой национальный цветок Японии?', 'Сакура', 'Ромашка', 'Дуб', 'Береза'))

app = QApplication([])

window = QWidget()
window.setWindowTitle('Memo Card')

'''Интерфейс приложения'''

btn_OK = QPushButton('Ответ')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

'''
Сейчас мы создадим направляющии линии и будем размещать на них наши объекты
'''

layout_ans1 = QHBoxLayout() #создали горизонтальную линию
'''Создали 2 вертикальные линии которые будут внутри горизонтальной '''
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout() 

layout_ans2.addWidget(rbtn_1) #Добавили переключатель к вертикальной линии
layout_ans2.addWidget(rbtn_2)

layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
'''К главной горизонтальной линии прикрепили две вертикальные 
к которым прикрепленны наши переключатель'''
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

'''
Добавляем к линии наш вопрос и размещаем его по центру нашего окна 
alignment <- отвечает за размещение окна
Qt.AlignHCenter <- Размещение по центру по горизонтали
Qt.AlignVCenter <- Размещение по центру по вертикали
'''
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

'''Ко второй линии мы должны прикрепить наш радиобокс'''
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

RadioGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)

layout_card.setSpacing(5)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Questions):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print(f'Статистика\n-Всего вопросов: {window.total} \n-Правильных ответов {window.score}')
        print(f'Рейтинг: {(window.score/window.total*100)}%')
    else:
        if answers[1].isChecked() or answers[2] or answers[3].isChecked():
            show_correct('Неверно!')
            print(f'Рейтинг: {(window.score/window.total*100)}%')

def next_question():
    window.total += 1
    print(f'Статистика\n-Всего вопросов: {window.total} \n-Правильных ответов {window.score}')
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.setLayout(layout_card)

window.total = 0
window.score = 0

btn_OK.clicked.connect(click_ok)
next_question()
window.show()
app.exec()
