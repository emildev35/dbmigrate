from dbconnection import getconnection
import xlsxwriter


conn = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')
cursor = conn.cursor()

sql = """
SELECT ACT_Codigo_Activo, ACT_No_Serie FROM Activos
WHERE ACT_No_Serie IN (
    SELECT ACT_No_Serie FROM Activos
    WHERE ACT_No_Serie IS NOT NULL AND ACT_No_Serie <> ''
    GROUP BY ACT_No_Serie
    HAVING COUNT(ACT_Codigo_Activo) > 1
)
"""

cursor.execute(sql)

datos = cursor.fetchall()

resultExcel = xlsxwriter.Workbook('Duplicados.xlsx')
sheet = resultExcel.add_worksheet()

sheet.write(0, 0, 'CODIGO')
sheet.write(0, 1, 'SERIE')

i = 0
for row in datos:
    j = 0
    for cell in row:
        sheet.write(i, j, cell)
        j += 1
    i += 1

resultExcel.close()
