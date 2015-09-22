from dbconnection import getconnection


conn = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Control')
conn_rrh = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')


cursor = conn.cursor()

cursor_rrhh = conn_rrh.cursor()



# cursor.execute("""
#     SELECT per.Ci, res.cod_act, res.fecha_asignacion
#     FROM TCTR_Persona per INNER JOIN Activos.dbo.TAF_RESPONSABLE res
#     ON (per.CodPersona=res.cod_funcionario)
#     """)
#
# cursor.execute("""
#     SELECT per.Ci
#     FROM TCTR_Persona per INNER JOIN Activos.dbo.TAF_RESPONSABLE res
#     ON (per.CodPersona=res.cod_funcionario)
#     """)

# cursor_rrhh.execute("""
#     SELECT PER_CI_Empleado FROM Personal
#     """)

# Verificar que existan todos lo funionarios
# list_data = cursor.fetchall()
# list_data_activos = cursor_rrhh.fetchall()


# A = set()
# B = set()

# for r in list_data:
#     A.add(r[0])


# for r in list_data_activos:
#     B.add(r[0])

# print A - B


cursor.execute("""
    SELECT per.Ci, res.cod_act, res.fecha_asignacion
    FROM TCTR_Persona per INNER JOIN Activos.dbo.TAF_RESPONSABLE res
    ON (per.CodPersona=res.cod_funcionario)
    """)


asignados = cursor.fetchall()

print len(asignados)

for r in asignados:
    ci = str(r[0])
    act = int(r[1][len(r[1])-4:len(r[1])])
    fecha = r[2]
    fecha = fecha.strftime('%Y-%d-%m')
    sql_data = 'UPDATE Activos set ACT_CI_Empleado_Asignado=\'%s\', ACT_Fecha_Asignacion=\'%s\' WHERE ACT_Codigo_Activo=%s' % (str(ci), fecha, int(act))
    try:
        cursor_rrhh.execute(sql_data)
        conn_rrh.commit()
    except Exception, e:
        pass
    print sql_data
