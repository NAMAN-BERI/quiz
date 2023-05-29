import openpyxl
wb = openpyxl.load_workbook('main.xlsx')

sheet = wb['USER']

def add_score(u_id,score):
    cell = sheet['F'+str(u_id)]
    old_score = cell.value
    cell.value = old_score + score
    wb.save('main.xlsx')