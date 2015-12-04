from dbconnection import getconnection
import xlrd


conn = getconnection('192.168.97.97', 'sa', 's4*Activos', 'Activos')
cursor = conn.cursor()

workbook = xlrd.open_workbook('excels/backup_error.xlsx')
activos_sheet = workbook.sheet_by_index(1)

sql = """
INSERT INTO Componentes (%s) VALUES(%s)
"""
rows = activos_sheet.nrows
header = []
values = []
for i in range(rows):
    values = []
    for j in range(activos_sheet.ncols):
        if 'Entrega' in str(activos_sheet.cell(0, j).value) or 'Comodato' in str(activos_sheet.cell(0, j).value):
            continue
        if 'Vencimiento' in str(activos_sheet.cell(0, j).value) or 'Comodato' in str(activos_sheet.cell(0, j).value):
            continue
        if 'Reval' in str(activos_sheet.cell(0, j).value) or 'Depre' in str(activos_sheet.cell(0, j).value):
            continue
        if 'Seguro' in str(activos_sheet.cell(0, j).value) or 'Comprobante' in str(activos_sheet.cell(0, j).value):
            continue
        if 'comodato' in str(activos_sheet.cell(0, j).value) or 'Comprobante' in str(activos_sheet.cell(0, j).value):
            continue
        if 'Mantenimiento' in str(activos_sheet.cell(0, j).value) or 'Comprobante' in str(activos_sheet.cell(0, j).value):
            continue
        if 'Folio' in str(activos_sheet.cell(0, j).value) or 'RUAT' in str(activos_sheet.cell(0, j).value):
            continue
        if 'Asig' in str(activos_sheet.cell(0, j).value) or 'Baja' in str(activos_sheet.cell(0, j).value):
            continue
        if 'Reso' in str(activos_sheet.cell(0, j).value) or 'Baja' in str(activos_sheet.cell(0, j).value):
            continue
        if i == 0:
            header.append(activos_sheet.cell(i, j).value)
        else:
            val = '\'\''
            if type(activos_sheet.cell(i, j).value) == str:
                val = '\'' + activos_sheet.cell(i, j).value + '\''
            if type(activos_sheet.cell(i, j).value) == float:
                val = str(int(activos_sheet.cell(i, j).value))
            if type(activos_sheet.cell(i, j).value) == unicode:
                val = '\'' + str(activos_sheet.cell(i, j).value.encode('ascii', 'ignore')) + '\''
            if type(activos_sheet.cell(i, j).value) == int:
                val = str(int(activos_sheet.cell(i, j).value))
            if 'Valor' in str(activos_sheet.cell(0, j).value) or 'Tipo_Cambio' in str(activos_sheet.cell(0, j).value):
                try:
                    val = str(activos_sheet.cell(i, j).value)
                except Exception:
                    pass
            if 'Fecha' in str(activos_sheet.cell(0, j).value):
                try:
                    val = '\'' + xlrd.xldate.xldate_as_datetime(activos_sheet.cell(i, j).value, workbook.datemode).strftime('%Y-%m-%d') + 'T00:00:00\''
                except Exception:
                    pass
            if 'Codigo' in str(activos_sheet.cell(0, j).value):
                try:
                    val = str(int(activos_sheet.cell(i, j).value) - 5)
                except Exception:
                    pass
            values.append('/*' + str(activos_sheet.cell(0, j).value) + '*/' + val)
    if i > 0:
        try:
            cursor.execute(sql % (','.join(header), ','.join(values)))
            conn.commit()
        except Exception, ex:
            conn.rollback()
            print ex
            print sql % (','.join(header), ','.join(values))
