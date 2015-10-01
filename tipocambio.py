from dbconnection import getconnection


conn = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Admin')
conn_act = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')


cursor = conn.cursor()
cursor_act = conn_act.cursor()

cursor.execute('SELECT c_moneda, n_tipocambio, d_fecha FROM t_tipocambio')
tipo_cambios = cursor.fetchall()
reso = ''

sql_ufv = """
    UPDATE Activos SET ACT_Tipo_Cambio_UFV=%s WHERE ACT_Fecha_Incorporacion='%s'
"""
sql_sus = """
    UPDATE Activos SET ACT_Tipo_Cambio_Dolar=%s WHERE ACT_Fecha_Incorporacion='%s'
"""
n_fallas = 0
for r in tipo_cambios:
    if r[0] == 'UFV':
        try:
            cursor_act.execute(sql_ufv % (r[1], r[2].strftime('%Y-%m-%d')))
            conn_act.commit()
        except Exception:
            print sql_ufv % (r[1], r[2].strftime('%Y-%m-%d'))
    else:
        try:
            cursor_act.execute(sql_sus % (r[1], r[2].strftime('%Y-%m-%d')))
            conn_act.commit()
        except Exception:
            print sql_sus % (r[1], r[2].strftime('%Y-%m-%d'))
