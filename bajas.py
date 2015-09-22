from .dbconnection import getconnection

conn = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Activos')
conn_act = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')

cursor = conn.cursor()
cursor_act = conn_act.cursor()
cursor.execute('SELECT * FROM TAF_BAJAS')
l_nuevos_val = cursor.fetchall()
reso = ''


for r in l_nuevos_val:
    r_reso = ''
    cod_activo = 0

    if 'AGIT/0037/2010' in r[4]:
        r_reso = 'AGIT/0037/2010'
    else:
        r_reso = r[4].replace(" ", "").strip()

    cod_activo = r[0][len(r[0]) - 4:len(r[0])]
    fecha_baja = r[3].strftime('%Y-%d-%m')
    sql = """
        UPDATE Activos.dbo.Activos
        SET  ACT_Fecha_Baja='%s', ACT_No_Resolucion_Baja='%s'
        WHERE  ACT_Codigo_Activo=%s
        """ % (fecha_baja, r_reso, cod_activo)
    try:
        cursor_act.execute(sql)
        conn_act.commit()
    except Exception, ex:
        pass
    # print sql
    if len(r_reso) > 20:
        print sql
