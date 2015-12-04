from dbconnection import getconnection
import xlsxwriter


conn = getconnection('192.168.97.97', 'sa', 's4*Activos', 'Activos')
cursor = conn.cursor(as_dict=True)

condicion = ' >= 5350'
sql = 'SELECT * FROM Activos WHERE ACT_Codigo_Activo %s ' % condicion

cursor.execute(sql)
activos = cursor.fetchall()

col, row = 0, 1

workbook = xlsxwriter.Workbook('excels/backup_norma.xlsx')
worksheet = workbook.add_worksheet()

for activo in activos:
    for key, data in activo.items():
        if row == 1:
            worksheet.write(0, col, key)
        worksheet.write(row, col, data)
        col += 1
    row += 1
    col = 0


worksheet_caracteristicas = workbook.add_worksheet()
sql_caracteristicas = 'SELECT * FROM Componentes WHERE COM_Codigo_Activo %s' % condicion

cursor.execute(sql_caracteristicas)
caracteristicas = cursor.fetchall()

col, row = 0, 1

for caracteristica in caracteristicas:
    for key, data in caracteristica.items():
        if row == 1:
            worksheet_caracteristicas.write(0, col, key)
        worksheet_caracteristicas.write(row, col, data)
        col += 1
    row += 1
    col = 0

worksheet_documento = workbook.add_worksheet()
sql_documento = 'SELECT * FROM Documentos_Respaldo WHERE DOR_Codigo_Activo %s' % condicion

cursor.execute(sql_documento)
documentos = cursor.fetchall()

col, row = 0, 1

for documento in documentos:
    for key, data in documento.items():
        if row == 1:
            worksheet_documento.write(0, col, key)
        worksheet_documento.write(row, col, data)
        col += 1
    row += 1
    col = 0

workbook.close()
