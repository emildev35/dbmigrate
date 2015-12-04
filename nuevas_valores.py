from dbconnection import getconnection
import xlrd


conn_activos = getconnection('192.168.97.97', 'sa', 's4*Activos', 'Activos')

cursor_activos = conn_activos.cursor()


sql_activos = """
    UPDATE Activos SET ACT_Valor_Compra=%s, ACT_Valor_Neto=%s, ACT_Actualizacion_Acumulada_Gestion_Anterior=%s
    WHERE ACT_Codigo_Activo=%d
"""

wb_asignaciones = xlrd.open_workbook('excels/arreglo_valores_02_12.xlsx')
asignacion = wb_asignaciones.sheet_by_index(0)


def getCodigo(oldCode):
    oldCode = str(int(oldCode))
    oldCode = oldCode[len(oldCode) - 4: len(oldCode)]
    return int(oldCode)

for i in range(asignacion.nrows):
    valor_compra = str(asignacion.cell(i, 1).value)
    # codigo = getCodigo(str(int(asignacion.cell(i, 0).value)))
    codigo = str(int(asignacion.cell(i, 0).value))
    try:
        cursor_activos.execute(sql_activos % (valor_compra, valor_compra, valor_compra, int(codigo)))
        conn_activos.commit()

    except Exception:
        print sql_activos % (ci, int(dependencia), int(codigo))
        conn_activos.rollback()
