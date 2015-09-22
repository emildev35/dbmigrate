from dbconnection import getconnection


conn_old = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Control')
conn_new = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'RecursosHumanos')


cursor = conn_old.cursor()
cursor.execute("""
    SELECT per.Ci, dp.p_nom, dp.s_nom, dp.ap_pat, dp.ap_mat,
    dp.email, dp.celu, pa.f_ing, pa.cod_unidad, pa.cod_regional
    FROM
    TCTR_Persona per
    INNER JOIN Registro.dbo.TRH_DATOSPERSONALES dp ON (per.CodPersona = dp.cod_per)
    INNER JOIN Registro.dbo.TRH_PUESTOACTUAL pa ON (per.CodPersona=pa.cod_per)""")
l_usuarios = cursor.fetchall()

for r in l_usuarios:
    print r


print len(l_usuarios)

