from dbconnection import getconnection


conn = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Activos')
conn_act = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')


cursor = conn.cursor(as_dict=True)
cursor_act = conn_act.cursor()
cursor.execute('SELECT * FROM TAF_REVALORIZACIONES')
l_nuevos_val = cursor.fetchall()


for resolucion in l_nuevos_val:
    print '*' * 30
    print resolucion['fecha_rev']
    print resolucion['valor_ac']
    print resolucion['cod_act']
    print resolucion['resolucion'].strip()
    print resolucion['nuevo_valor']
