from dbconnection import getconnection
import xlsxwriter


conn = getconnection('192.168.97.97', 'sa', 's4*Activos', 'Activos')
cursor = conn.cursor(as_dict=True)

sql = 'SELECT * FROM Activos WHERE ACT_Codigo_Activo > 5111'

cursor.execute(sql)
activos = cursor.fetchall()

col, row = 0, 0

workbook = xlsxwriter.Workbook('excels/backup.xlsx')
worksheet = workbook.add_worksheet()

for activo in activos:
    for key, data in activo.items():
        if row == 0:
            worksheet.write(row, col, key)
        else:
            worksheet.write(row, col, data)
        col += 1
    row += 1
    col = 0


worksheet_caracteristicas = workbook.add_worksheet()
sql_caracteristicas = 'SELECT * FROM Componentes WHERE COM_Codigo_Activo > 5111'

cursor.execute(sql_caracteristicas)
caracteristicas = cursor.fetchall()

col, row = 0, 0

for caracteristica in caracteristicas:
    for key, data in caracteristica.items():
        if row == 0:
            worksheet_caracteristicas.write(row, col, key)
        else:
            worksheet_caracteristicas.write(row, col, data)
        col += 1
    row += 1
    col = 0

workbook.close()
