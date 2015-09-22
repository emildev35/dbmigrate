import xlrd
import datetime as dt
from dbconnection import getconnection


conn = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')
cursor = conn.cursor()

# workbook = xlrd.open_workbook('activosbajas.xls')
# bajas = workbook.sheet_by_index(0)

# sql = """
    # UPDATE Activos SET ACT_No_Resolucion_Baja='%s'
    # WHERE ACT_Codigo_Activo=%d
# """
# n_fail = 0

# for i in range(0, bajas.nrows):
    # idActivo = bajas.cell(i, 0).value
    # idActivo = str(int(idActivo))
    # idActivo = idActivo[len(idActivo) - 4: len(idActivo)]
    # motivo = bajas.cell(i, 3).value.replace('\n', '')
    # resolucion = bajas.cell(i, 9).value
    # try:
        # cursor.execute(sql % (resolucion, int(idActivo)))
        # conn.commit()
    # except Exception:
        # print sql % (resolucion, int(idActivo))
        # n_fail += 1

# print 'No registrados %d' % n_fail


workbook = xlrd.open_workbook('bajasindividuales.xls')
bajas = workbook.sheet_by_index(0)

sql = """
    UPDATE Activos SET ACT_Fecha_Baja='%s', ACT_Valor_Neto=%s
    WHERE ACT_Codigo_Activo=%d
"""
n_fail = 0

for i in range(0, bajas.nrows):
    idActivo = bajas.cell(i, 0).value
    idActivo = str(int(idActivo))
    idActivo = idActivo[len(idActivo) - 4: len(idActivo)]
    fecha = xlrd.xldate.xldate_as_tuple(bajas.cell(i, 8).value, workbook.datemode)
    fecha_baja = dt.datetime(fecha[0], fecha[1], fecha[2])
    valor_neto = bajas.cell(i, 15).value
    try:
        cursor.execute(sql % (fecha_baja.strftime('%Y-%d-%m'), valor_neto, idActivo))
        conn.commit()
    except Exception:
        print sql % (fecha_baja.strftime('%Y-%d-%m'), valor_neto, int(idActivo))
        n_fail += 1

print 'No registrados %d' % n_fail
