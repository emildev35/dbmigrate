from dbconnection import getconnection
import xlrd


conn = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Registro')
cursor = conn.cursor()

cursor.execute("""
    SELECT DISTINCT dts.cod_per, dts.nro_doc, res.cod_act, res.*
    FROM TRH_DATOSPERSONALES dts INNER JOIN
    Activos.dbo.TAF_RESPONSABLE res ON (dts.cod_per = res.cod_funcionario)
    """)

asignaciones = cursor.fetchall()

for asig in asignaciones:
    print asig
