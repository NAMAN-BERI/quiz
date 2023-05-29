import openpyxl
import questions
wb = openpyxl.load_workbook('main.xlsx')

sheet = wb['G.K QUIZ']

def get_q(u_id):
    
    q_no = 1
    number_q = int(input("NUMBER OF QUESTIONS: "))
    questionss =[]
    for i in range(0,number_q):
        q_no += 1
        question = []
        questionss.append(question_data(question,q_no))
    score = questions.ask_questions(questionss,number_q)
    return score


def question_data(question,q_no):
    question.append(sheet['A'+str(q_no)].value)
    question.append(sheet['B'+str(q_no)].value)
    question.append(sheet['C'+str(q_no)].value)
    question.append(sheet['E'+str(q_no)].value)
    question.append(sheet['G'+str(q_no)].value)
    question.append(sheet['I'+str(q_no)].value)
    question.append(sheet['K'+str(q_no)].value)
    question.append(sheet['L'+str(q_no)].value)
    return question

