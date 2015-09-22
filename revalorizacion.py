from dbconnection import getconnection


conn = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Activos')
conn_act = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')


cursor = conn.cursor()
cursor_act = conn_act.cursor()
cursor.execute('SELECT * FROM TAF_REVALORIZACIONES')
l_nuevos_val = cursor.fetchall()
reso = ''

for r in l_nuevos_val:
    r_reso = ''
    cod_activo = 0
    if 'AGIT/0037/2010' in r[3]:
        r_reso = 'AGIT/0037/2010'
    else:
        r_reso = r[3].replace(" ", "").strip()

    cod_activo = r[1][len(r[1])-4:len(r[1])]
    sql = """
            UPDATE Activos.dbo.Activos
            SET  ACT_No_Resolucion='%s', ACT_Fecha_Ultima_Revalorizacion='%s',
            ACT_Actualizacion_Acumulada_Gestion_Anterior=%d,
            ACT_Valor_Neto=%d
            WHERE  ACT_Codigo_Activo=%s
        """ % (r_reso, '2010-08-13', r[2], r[6], cod_activo)
    try:
        cursor_act.execute(sql)
        conn_act.commit()
    except Exception, e:
        print sql

