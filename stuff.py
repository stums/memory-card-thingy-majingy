from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QHBoxLayout,QPushButton,QRadioButton,QGroupBox,QButtonGroup
from random import *
app = QApplication([])
window = QWidget()
window.setWindowTitle("Kahoot 2.1")
window.resize(500,400)

class Question:
    def __init__(self,question,right, w1, w2, w3):
        self.question = question
        self.right = right
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3

question_list = []
question_list.append(Question("What is 1 + 1?", "2", "3", "1","0"))
question_list.append(Question("What is the longest english word","supercalifragilisticexpealodocious", "onomatopoeai","wompus","."))
question_list.append(Question("What is the shortest english word","a",".",",","]"))
question_list.append(Question("What is the largest desert in the world","Antarctica","Sahara Desert","My Backyard","stuff"))
question_list.append(Question("What is the tallest tower in the world","Burj Khalifa","Tokyo Skytree","Eiffel Tower", "My meemaw's house"))
question_list.append(Question("What is the deepest point in the Ocean","Mariana Trench","My swimming pool","The middle of the atlantic ocean","The Pacific Ocean"))
question_list.append(Question("What is the smallest country in the world","Vatican City","Italy","Germany","Cuba"))
question_list.append(Question("Where was Cristiano Ronaldo From?","Portugal","Monaco","Russia","Spain"))
question_list.append(Question("How many countries are there?","195","203","186","217"))
question_list.append(Question("What is the most popular game?","Minecraft","GTA V","Fortnite","Valorant"))





question_text = QLabel("How much time does Jett smoke last?")
radioGroup = QGroupBox("Answer Options:")
ansGroup = QGroupBox("Results:")
results_text = QLabel("Correct or Incorrect")
ans1 = QLabel("Answer will be here soon.....")
radio1 = QRadioButton("5 Seconds")
radio2 = QRadioButton("10 Seconds")
radio3 = QRadioButton("2 Seconds")
radio4 = QRadioButton("4 Seconds")
btn = QPushButton("Answer")
score1 = QLabel("Score: 0")
rating = QLabel("Rating: 0")
buttonGroup = QButtonGroup()
buttonGroup.addButton(radio1)
buttonGroup.addButton(radio2)
buttonGroup.addButton(radio3)
buttonGroup.addButton(radio4)

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QVBoxLayout()
row4 = QVBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
anscol1 = QVBoxLayout()

col1.addWidget(radio1)
col2.addWidget(radio2)
col1.addWidget(radio3)
col2.addWidget(radio4)

row3.addWidget(score1)
row4.addWidget(rating)

anscol1.addWidget(ans1)

row1.addLayout(col1)
row1.addLayout(col2)


radioGroup.setLayout(row1)
radioGroup.setLayout(row3)

col3 = QVBoxLayout()
col3.addWidget(results_text, alignment=Qt.AlignCenter)
col3.addWidget(ans1, alignment=Qt.AlignCenter)

ansGroup.setLayout(col3)


r1 = QHBoxLayout()
r2 = QHBoxLayout()
r3 = QHBoxLayout()

r1.addWidget(question_text,alignment=Qt.AlignCenter)
r2.addWidget(radioGroup)
r2.addWidget(ansGroup)
ansGroup.hide()
r3.addWidget(btn)


master = QVBoxLayout()
master.addLayout(r1)
master.addLayout(r2)
master.addLayout(r3)
master.addLayout(row3)
master.addLayout(row4)

window.setLayout(master)

def show_answer():
    radioGroup.hide()
    ansGroup.show()
    btn.setText("Next Question")

def next_question():
    window.total += 1
    print("Statistics:\n- Total Questions",window.total,"\n-Correct Answers:",window.score)
    current = randint(0,len(question_list)-1)
    q = question_list[current]
    ask(q)



def show_question():
    ansGroup.hide()
    radioGroup.show()
    btn.setText("Answer")

    buttonGroup.setExclusive(False)
    radio1.setChecked(False)
    radio2.setChecked(False)
    radio3.setChecked(False)
    radio4.setChecked(False)
    buttonGroup.setExclusive(False)



def test():
    if btn.text() == "Answer":
        check_answer()
    else:
        next_question()



answers = [radio1, radio2, radio3, radio4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.w1)
    answers[2].setText(q.w2)
    answers[3].setText(q.w3)
    question_text.setText(q.question)
    ans1.setText(q.right)
    show_question()

shuffle(question_list)
def show_correct(res):
    results_text.setText(res)
    show_answer()

def check_answer():
    if answers[0].isChecked():
        show_correct("Correct!")
        window.score +=1
        score1.setText("Score:"+str(window.score))
        rating.setText("Rating"+str(window.score/window.total*100)+"%")
        print("Statistics:\n- Total Question",window.total,"\n Correct Asnwers:",window.score)
        print("Rating:",round(window.score/window.total*100,1),"%")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            rating.setText("Rating:"+str(round(window.score/window.total*100))+"%")
            print("Rating:",round(window.score/window.total*100,1),"%" )
            show_correct("Incorrect")



window.total = 0
window.score = 0
next_question()
btn.clicked.connect(test)
window.show()
app.exec_()