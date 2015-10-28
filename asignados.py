from dbconnection import getconnection

conn = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Registro')
conn_rrh = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'RecursosHumanos')

cursor = conn.cursor()

cursor_rrhh = conn_rrh.cursor()

cursor.execute("""
    SELECT DISTINCT dts.cod_per, dts.nro_doc
    FROM TRH_DATOSPERSONALES dts INNER JOIN
    Activos.dbo.TAF_RESPONSABLE res ON (dts.cod_per = res.cod_funcionario)
    """)


cursor_rrhh.execute("""
    SELECT PER_CI_Empleado FROM Personal
    """)

# Verificar que existan todos lo funcionarios
list_data = cursor.fetchall()
list_data_activos = cursor_rrhh.fetchall()

A = []
B = []
C = []
for l in list_data_activos:
    A.append(l[0])

for func in list_data:
    if func[1] in A:
        B.append(func[1])
    else:
        C.append(func[1])

print "Total de Usuario: %d" % len(list_data_activos)
print "Usuarios Encontrados: %d" % len(B)
print "Usuarios no Registrados: %d" % len(C)

cursor.execute("""
    SELECT dts.cod_per, dts.nro_doc, res.cod_act, res.fecha_asignacion
    FROM TRH_DATOSPERSONALES dts INNER JOIN
    Activos.dbo.TAF_RESPONSABLE res ON (dts.cod_per = res.cod_funcionario)
    WHERE res.estado = 1
    """)

lista_asignador = cursor.fetchall()

sql = """
    UPDATE Activos SET ACT_CI_Empleado_Asignado='%s', ACT_Fecha_Asignacion='%s'
    WHERE ACT_Codigo_Activo = %s
"""

conn_rrh = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')

cursor_rrhh = conn_rrh.cursor()

for asig in lista_asignador:
    try:
        cursor_rrhh.execute(sql % (asig[1], asig[3].strftime('%Y-%m-%d'), asig[2][len(asig[2]) - 4:len(asig[2])]))
        conn_rrh.commit()
    except Exception, ex:
        print ex
        # print sql % (asig[1], asig[3].strftime('%Y-%m-%d'), asig[2][len(asig[2]) - 4:len(asig[2])])

print len(lista_asignador)
