from dbconnection import getconnection
import xlsxwriter


conn = getconnection('192.168.97.97', 'sa', 's4*Activos', 'Activos')
cursor = conn.cursor()

conn_a = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Activos')
cursor_a = conn_a.cursor()

cursor_a.execute("SELECT cod_act, descripcion FROM TAF_ACTIVO WHERE cod_act <> 0")
nombres = cursor_a.fetchall()

sql = 'SELECT ACT_Nombre_Activo FROM Activos WHERE ACT_Codigo_Activo=\'%s\''


def getCodigo(oldCode):
    oldCode = str(int(oldCode))
    oldCode = oldCode[len(oldCode) - 4: len(oldCode)]
    return int(oldCode)

r = 0

file_xls = xlsxwriter.Workbook('nombre_erroneos.xlsx')
sheet = file_xls.add_worksheet()

row = 0

for activo in nombres:
    codigo = getCodigo(activo[0])
    nombre = activo[1].encode('ascii', 'ignore').strip().replace('\n', '').replace('\r', '').replace('\t', '')
    cursor.execute(sql % codigo)
    nuevo_nombre = cursor.fetchone()
    if nuevo_nombre is None:
        sheet.write(row, 0, codigo)
        sheet.write(row, 1, 'NO EXISTE (NUEVO)')
        sheet.write(row, 2, nombre)
        row += 1

    else:
        nuevo_nombre = nuevo_nombre[0].strip()
        if nombre.strip()[:5] != nuevo_nombre.strip()[:5]:
            sheet.write(row, 0, codigo)
            sheet.write(row, 1, 'NO COINSIDE')
            sheet.write(row, 2, nombre)
            sheet.write(row, 3, nuevo_nombre)
            row += 1
            r += 1

file_xls.close()
print '%d diferentes' % r
