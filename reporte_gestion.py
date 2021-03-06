from dbconnection import getconnection
import xlsxwriter


conn_a = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Activos')
cursor_a = conn_a.cursor()

cursor_a.execute("""
    SELECT cod_act, descripcion, vida_util, fecha_inc, fecha_compra, valor, regional
    FROM TAF_ACTIVO
    WHERE cod_act <> 0 AND fecha_inc > '2013-12-31T00:00:00' AND fecha_inc < '2014-01-01T00:00:00'
""")

nombres = cursor_a.fetchall()


def getCodigo(oldCode):
    oldCode = str(int(oldCode))
    oldCode = oldCode[len(oldCode) - 4: len(oldCode)]
    return int(oldCode)

r = 0

file_xls = xlsxwriter.Workbook('excels/activos_2015.xlsx')
sheet = file_xls.add_worksheet()

row = 0

for activo in nombres:
    for i in range(len(activo)):
        sheet.write(row, i, activo[i])
    row += 1


file_xls.close()
print '%d diferentes' % r
# sql = 'UPDATE Activos set ACT_Nombre_Activo=\'%s\' WHERE ACT_Codigo_Activo=\'%s\''
