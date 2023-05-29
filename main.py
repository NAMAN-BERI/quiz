import openpyxl
import user
import domain
import scores
wb = openpyxl.load_workbook('main.xlsx')

sheet = wb['USER']

u_id = user.user()

score = domain.get_q(u_id)

scores.add_score(u_id,score)