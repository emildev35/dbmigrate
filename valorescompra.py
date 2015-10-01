from dbconnection import getconnection


conn = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Activos')
conn_act = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')
cursor = conn.cursor()
cursor_act = conn_act.cursor()

cursor.execute('SELECT cod_act, valor FROM TAF_ACTIVO')

lista = cursor.fetchall()

sql = """
UPDATE Activos SET ACT_Valor_Compra=%d
WHERE ACT_Codigo_Activo = %s
"""

conn_er = 1

for act in lista:
    codigo = act[0][len(act[0]) - 4: len(act[0])]
    valor = act[1]
    try:
        cursor_act.execute(sql % (valor, codigo))
        conn_act.commit()
    except Exception:
        print sql % (valor, codigo)
        conn_er += 1

print 'Erroneso :  %d' % conn_er
