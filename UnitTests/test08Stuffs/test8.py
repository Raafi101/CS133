from tkinter import *
import readquiz as rq
import random

#Data =====================================================
questions = rq.loadQuestions()
questionsAnswered = 0
correct = 0
feedback = ''

def getNewQuestion():
    random.shuffle(questions) #*Resubmitted to use random.shuffle instead of random.choice*
    question = questions[0]
    actQuestion['text'] = question[1]
    if question[0] == True:
        yes['command'] = goodAnswer
        no['command'] = badAnswer
    else:
        no['command'] = goodAnswer
        yes['command'] = badAnswer

#goodAnswer and badAnswer update the text within the function
def goodAnswer():
    global correct, questionsAnswered, feedback
    correct += 1
    questionsAnswered += 1
    score['text'] = 'Score: {0}/{1}'.format(correct, questionsAnswered)
    status['text'] = 'Your answer was correct'
    status['bg'] = 'light green'
    getNewQuestion()

def badAnswer():
    global correct, questionsAnswered, feedback
    correct += 0
    questionsAnswered += 1
    score['text'] = 'Score: {0}/{1}'.format(correct, questionsAnswered)
    status['text'] = 'Your answer was incorrect'
    status['bg'] = 'pink'
    getNewQuestion()

#Window ===================================================
root = Tk()
root['bg'] = 'light gray'
root.title('Quiz')

#Question -------------------------------------------------
questionFrame = Frame(root)
questionFrame['bg'] = 'light gray'

#questionLabel
questionLabel = Label(questionFrame)
questionLabel['text'] = 'Question:'
questionLabel['bg'] = 'light gray'
questionLabel.pack(side = TOP)

#Actual question
actQuestion = Message(questionFrame, width = 250)
actQuestion['bg'] = 'light gray'
initQuestion = random.choice(questions)
actQuestion['text'] = initQuestion[0]
actQuestion.pack()

#Yes ------------------------------------------------------
yesFrame = Frame(root)
yesFrame['bg'] = 'light gray'

#yes button
yes = Button(yesFrame)
yes['text'] = 'Yes'
yes['bg'] = 'light gray'
yes.pack(fill = X)

#No -------------------------------------------------------
noFrame = Frame(root)
noFrame['bg'] = 'light gray'

#no button
no = Button(noFrame)
no['text'] = 'No'
no['bg'] = 'light gray'
no.pack(fill = X)

#initialize button commands -------------------------------
if initQuestion[0] == True:
    yes['command'] = goodAnswer
    no['command'] = badAnswer
else:
    no['command'] = goodAnswer
    yes['command'] = badAnswer

#Status ---------------------------------------------------
statusFrame = Frame(root)
statusFrame['bg'] = 'light gray'

#status
status = Label(statusFrame)
status['bg'] = 'light gray'
status['text'] = 'Status'
status.pack(side = LEFT, anchor = W)

#score
score = Label(statusFrame)
score['bg'] = 'light gray'
score['text'] = 'Score: 0/0'
score.pack(side = RIGHT, anchor = E)

#Frames ---------------------------------------------------
questionFrame.pack(side = TOP, expand = YES, fill = BOTH)
statusFrame.pack(side = BOTTOM, expand = YES, fill = BOTH)
yesFrame.pack(side = LEFT, expand = YES, fill = BOTH)
noFrame.pack(side = RIGHT, expand = YES, fill = BOTH)

getNewQuestion()
mainloop()