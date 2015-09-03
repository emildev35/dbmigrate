from dbconnection import getconnection, getTipoCambioDolar
from dbconnection import getIdProveedor, getDependencia, getTipoCambioUfv
from dbconnection import insertData
from settings import DB_ORIGIN, DB_DESTINT

conn_source = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Activos')
conn_st = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Admin')
conn = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')

cursor = conn.cursor(as_dict=True)

cursor_source = conn_source.cursor(as_dict=True)

sql_select_origin = \
    'SELECT %s FROM TAF_ACTIVO' % (','.join(DB_ORIGIN['COLUMNS']))


cursor_source.execute(sql_select_origin)
list_activos_a = cursor_source.fetchall()

for row in list_activos_a:
    row['cod_prov'] = getIdProveedor(conn_source, row['cod_prov'])[0]
    row['regional'] = getDependencia(row['regional'])
    row['tipo_cambio_ufv'] = getTipoCambioUfv(conn_st, row['fecha_inc'])[0]
    row['tipo_cambio_dolar'] = getTipoCambioDolar(conn_st, row['fecha_inc'])[0]
    if row['cod_aux'] == 59:
        row['cod_grupo'] = 3
    if row['cod_aux'] == 59:
        row['cod_grupo'] = 3


sql_insert = \
    'INSERT INTO Activos(%s)' % (','.join(DB_DESTINT['COLUMNS']))

for activo in list_activos_a:
    insertData(conn, sql_insert, activo)

print "Numero de Activos Leidos " + str(len(list_activos_a))








cursor.execute('SELECT * FROM Activos')
list_activos = cursor.fetchall()
