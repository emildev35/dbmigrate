from dbconnection import getconnection
import xlrd


conn = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')
cursor = conn.cursor()

excelFile = xlrd.open_workbook('Listado_Series_PC.xls')
sheet = excelFile.sheet_by_index(1)

sql = 'UPDATE Activos set ACT_No_Serie=\'%s\' WHERE ACT_Codigo_Activo=%d'

ncols = sheet.ncols
for i in range(1, sheet.nrows):
    codigo = int(sheet.cell(i, 1).value)
    serie = str(sheet.cell(i, 2).value)
    cursor.execute(sql % (serie, codigo))

    codigo = int(sheet.cell(i, 3).value)
    serie = str(sheet.cell(i, 4).value)
    cursor.execute(sql % (serie, codigo))

    codigo = int(sheet.cell(i, 5).value)
    serie = str(sheet.cell(i, 6).value)
    cursor.execute(sql % (serie, codigo))

    try:
        conn.commit()
    except Exception, ex:
        print ex
