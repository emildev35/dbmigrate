from dbconnection import getconnection


conn = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Activos')
conn_act = getconnection('192.168.97.99\\DESARROLLO', 'sa', 'ADMDesarrollo2015*', 'Activos')
cursor = conn.cursor()
cursor_act = conn_act.cursor()

cursor.execute('SELECT cod_act, valor FROM TAF_ACTIVO')

lista = cursor.fetchall()

sql = """
UPDATE Activos SET ACT_Valor_Compra=%s, ACT_Valor_Neto=%s, ACT_Actualizacion_Acumulada_Gestion_Anterior=%s,
ACT_Depreciacion_Acumulada_Gestion_Anterior=0, ACT_Actualizacion_Gestion_Actual=0,
ACT_Depreciacion_Gestion_Actual=0, ACT_Vida_Residual=ACT_Vida_Util,
ACT_Fecha_Ultima_Depreciacion=ACT_Fecha_Incorporacion,
ACT_Actualizacion_Depreciacion_Acumulada=0,
ACT_Fecha_Baja=NULL, ACT_Fecha_Ultima_Revalorizacion=NULL, ACT_No_Resolucion=NULL,
ACT_No_Resolucion_Baja=NULL
WHERE ACT_Codigo_Activo = %s;
UPDATE Activos SET ACT_Valor_Compra=5001829.58, ACT_Valor_Neto=5001829.58,
ACT_Actualizacion_Acumulada_Gestion_Anterior=5001829.85 WHERE ACT_Codigo_Activo=3769;
DELETE FROM Cierre_Gestion WHERE CGE_Fecha_Cierre_Gestion > '2004-01-01T00:00:00'
"""

conn_er = 1

for act in lista:
    codigo = act[0][len(act[0]) - 4: len(act[0])]
    valor = act[1]
    try:
        cursor_act.execute(sql % (valor, valor, valor, codigo))
        conn_act.commit()
    except Exception, ex:
        print sql % (valor, valor, valor, codigo)
        conn_er += 1
        print ex

print 'Erroneos :  %d' % conn_er
