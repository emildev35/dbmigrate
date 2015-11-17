from dbconnection import getconnection
import math
import xlrd


conn_nuevo = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')
cursor_nuevo = conn_nuevo.cursor()

sql_insertC = """
    INSERT INTO C_Movimientos(
    CMV_Dependencia, CMV_Tipo_Movimiento, CMV_No_Documento, CMV_Unidad_Organizacional_Solicitante,
    CMV_CI_Solicitante, CMV_Tipo_Documento_Referencia, CMV_No_Documento_Referencia, CMV_Fecha_Registro,
    CMV_Fecha_Movimiento, CMV_Fecha_Documento_Referencia)
    VALUES(1, 15, 2, 1, 2381254, 7, '%s', '%s', '%s')
    """

sql_insertD = """
    INSERT INTO D_Movimientos(DMV_Dependencia, DMV_Tipo_Movimiento, DMV_No_Documento,  DMV_Codigo_Activo,
    DMV_Unidad_Organizacional, DMV_Fecha_Registro, DMV_Nueva_Vida_Util, DMV_Nuevo_Valor)
    VALUES(1, 15, 2, %d, 1, '%s', '%s', '%s')
    """

workbook = xlrd.open_workbook('REVALORIZADOSREVISADO.xls')
revalorizaciones = workbook.sheet_by_index(0)

fecha = '2010-08-10T00:00:00'
nro_resolucion = 'AGIT/0037/2010'


def getCodigo(oldCode):
    oldCode = str(int(oldCode))
    oldCode = oldCode[len(oldCode) - 4: len(oldCode)]
    return int(oldCode)


for i in range(revalorizaciones.nrows):
    try:
        cod = getCodigo(revalorizaciones.cell(i, 0).value)
        nueva_vida = int(math.floor(revalorizaciones.cell(i, 6).value))
        nueva_valor = revalorizaciones.cell(i, 8).value
        print cod
        print nueva_vida
        print nueva_valor
        print '*0*' * 30
        if i == 1:
            cursor_nuevo.execute(sql_insertC % (nro_resolucion, fecha, fecha, fecha))
            conn_nuevo.commit()
        cursor_nuevo.execute(sql_insertD % (cod, fecha, nueva_vida, nueva_valor))
        conn_nuevo.commit()
    except Exception, ex:
        print ex
