import openpyxl

wb = openpyxl.load_workbook('main.xlsx')

sheet = wb['G.K QUIZ']

def ask_questions(questions,number_q):
    score = 0
    for question in questions:  
        answer = []
        print()
        print("DIFFICULTY LEVEL-: ", question[1] )
        print()
        for i in range(2,7):
            if i == 2:
                print("Q) ", question[i])
                continue
            print((i-2), ")", question[i])

        option = int(input("ENTER THE OPTION: "))

        if question[7] == 1:
            answer.append(sheet['E'+str(question[0])].value)
            answer.append(1)
        elif question[7] == 2:
            answer.append(sheet['G'+str(question[0])].value)
            answer.append(2)
        elif question[7] == 3:
            answer.append(sheet['I'+str(question[0])].value)
            answer.append(3)
        else:
            answer.append(sheet['K'+str(question[0])].value)
            answer.append(4)

        if answer[1] == option:
            print("CORRECT ANSWER")
            print(answer[0])
            score += 1 
        else :
            print("WRONG ANSWER")
            print("CORRECT ANSWER IS: ", answer[0])
    print("YOUR SCORE IS ",score," OUT OF ",number_q)        
    return score