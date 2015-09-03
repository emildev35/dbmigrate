from dbconnection import getconnection, getIdProveedor, getDependencia
from dbconnection import getTipoCambioDolar, getTipoCambioUfv, insertData
from settings import DB_ORIGIN, DB_DESTINT

conn = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')

conn_source = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Activos')


c_origen = conn.cursor()
c_origen.execute("SELECT ACT_Codigo_Activo FROM Activos")
A = []
l_a = c_origen.fetchall()

for r in l_a:
    A.append(int(str(r[0])))


c_des = conn_source.cursor()
c_des.execute("SELECT cod_act FROM TAF_ACTIVO")
B = []
l_b = c_des.fetchall()

for r in l_b:
    B.append(int(str(r[0])[len(str(r[0]))-4:len(str(r[0]))]))


C = set(B) - set(A)


D = []

for r in l_b:
    if int(str(r[0])[len(str(r[0]))-4:len(str(r[0]))]) in C:
        D.append(r[0])

sql_select_origin =\
    'SELECT %s FROM TAF_ACTIVO' % (','.join(DB_ORIGIN['COLUMNS']))

str_where = ','.join(D)


c_list = conn_source.cursor(as_dict=True)
c_list.execute(sql_select_origin + ' WHERE cod_act IN(%s)' % str_where)
list_activos_a = c_list.fetchall()

print len(D)

for row in list_activos_a:
    row['cod_prov'] = getIdProveedor(conn_source, row['cod_prov'])[0]
    row['regional'] = getDependencia(row['regional'])
    row['tipo_cambio_ufv'] = getTipoCambioUfv(conn, row['fecha_inc'])[0]
    row['tipo_cambio_dolar'] = getTipoCambioDolar(conn, row['fecha_inc'])[0]
    if row['cod_aux'] == 59:
        row['cod_grupo'] = 3
    if row['cod_aux'] in (80, 104, 103, 81):
        row['cod_grupo'] = 2
    if row['cod_aux'] in (20, 21):
        row['cod_grupo'] = 1
    if row['cod_aux'] in (60, 74, 63):
        row['cod_grupo'] = 1
    if row['cod_fuente'] == 0:
        row['cod_fuente'] = 1
    if row['cod_organismo'] == 0:
        row['cod_organismo'] = 1

sql_insert = \
    'INSERT INTO Activos(%s)' % (','.join(DB_DESTINT['COLUMNS']))

for activo in list_activos_a:
    insertData(conn, sql_insert, activo)
