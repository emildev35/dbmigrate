from dbconnection import getconnection
import xlrd


conn_rrhh = getconnection('192.168.97.97', 'sa', 's4*Activos', 'RecursosHumanos')
conn_activos = getconnection('192.168.97.97', 'sa', 's4*Activos', 'Activos')

cursor_rrhh = conn_rrhh.cursor()
cursor_activos = conn_activos.cursor()

sql_depedencia = """
    SELECT PER_Dependencia FROM Personal WHERE PER_CI_Empleado='%s'
"""

sql_activos = """
    UPDATE Activos SET ACT_CI_Empleado_Asignado='%s', ACT_Dependencia=%d WHERE ACT_Codigo_Activo=%d
"""

wb_asignaciones = xlrd.open_workbook('excels/nuevas_asignaciones.xls')
asignacion = wb_asignaciones.sheet_by_index(2)


def getCodigo(oldCode):
    oldCode = str(int(oldCode))
    oldCode = oldCode[len(oldCode) - 4: len(oldCode)]
    return int(oldCode)

for i in range(asignacion.nrows):
    ci = str(int(asignacion.cell(i, 0).value))
    codigo = getCodigo(str(int(asignacion.cell(i, 1).value)))

    cursor_rrhh.execute(sql_depedencia % ci)
    dependencia = cursor_rrhh.fetchone()[0]

    try:
        cursor_activos.execute(sql_activos % (ci, int(dependencia), int(codigo)))
        conn_activos.commit()

    except Exception:
        print sql_activos % (ci, int(dependencia), int(codigo))
        conn_activos.rollback()
