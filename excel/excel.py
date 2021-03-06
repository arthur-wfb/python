import xlsxwriter
from db.DB import DB

db = DB()

tests = db.getAllTestResults()

workbook = xlsxwriter.Workbook('example.xlsx')
worksheet = workbook.add_worksheet()

cellPass = workbook.add_format(dict(font_color='green'))
failPass = workbook.add_format(dict(font_color='red', bold=True))

worksheet.write('A1', '№')
worksheet.write('B1', 'Название теста')
worksheet.write('C1', 'Успех')
worksheet.write('D1', 'Фиаско')
worksheet.write('E1', 'Дата')

for i, test in enumerate(tests):
    worksheet.write('A' + str(i+2), i+1)
    worksheet.write('B' + str(i + 2), test['test'])
    if test['result'] == 'passed':
        worksheet.write('C' + str(i + 2), 1, cellPass)
    else:
        worksheet.write('D' + str(i + 2), 1, failPass)
    worksheet.write('E' + str(i + 2), str(test['date']))

worksheet.write('F1', 'Успешные')
worksheet.write('G1', 'Неуспешные')
worksheet.write('F2', '=SUM(C:C)')
worksheet.write('G2', '=SUM(D:D)')

chart = workbook.add_chart(dict(type='column'))
chart.add_series(dict(values='=Sheet1!$F2'))
chart.add_series(dict(values='=Sheet1!$G2'))
chart.set_title(dict(name='Results'))
chart.set_style(37)
chart.set_plotarea(dict(
    border={'color': 'red', 'width': 2, 'dash_type': 'dash'},
    fill={'color': '#FFFFC2'}
))
worksheet.insert_chart('H7', chart)

worksheet.insert_chart('H7', chart)

workbook.close()