from dbconnection import getconnection
import xlsxwriter


conn = getconnection('192.168.97.97', 'sa', 's4*Activos', 'Activos')
cursor = conn.cursor()

conn_a = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Activos')
cursor_a = conn_a.cursor()

cursor_a.execute("SELECT cod_act, descripcion, vida_util, fecha_inc, fecha_compra, valor, regional FROM TAF_ACTIVO WHERE cod_act <> 0")
nombres = cursor_a.fetchall()

sql = 'SELECT ACT_Nombre_Activo FROM Activos WHERE ACT_Codigo_Activo=\'%s\''


def getCodigo(oldCode):
    oldCode = str(int(oldCode))
    oldCode = oldCode[len(oldCode) - 4: len(oldCode)]
    return int(oldCode)

r = 0

file_xls = xlsxwriter.Workbook('excels/activos_n.xlsx')
sheet = file_xls.add_worksheet()

row = 0

for activo in nombres:
    codigo = getCodigo(activo[0])
    cursor.execute(sql % codigo)
    nuevo_codigo = cursor.fetchone()
    if nuevo_codigo is None:
        continue
    nuevo_codigo = str(nuevo_codigo[0].encode('utf8', 'ignore'))
    if nuevo_codigo[:4] != activo[1][:4]:
        print nuevo_codigo
        print activo[1]
        for i in range(len(activo)):
            sheet.write(row, i, activo[i])
        row += 1


file_xls.close()
print '%d diferentes' % r
# sql = 'UPDATE Activos set ACT_Nombre_Activo=\'%s\' WHERE ACT_Codigo_Activo=\'%s\''
