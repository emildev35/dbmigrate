from dbconnection import getconnection
from dateutil.relativedelta import relativedelta


conn_old = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'ACTIVOS')
conn_new = getconnection('192.168.97.97', 'sa', 's4*Activos', 'Activos')
cursor_old = conn_old.cursor()
cursor_new = conn_new.cursor()
cursor_old.execute("""
    SELECT * FROM  TAF_SERIEACTIVO""")
lSeries = cursor_old.fetchall()

sqlGetData = 'SELECT ACT_Fecha_Compra FROM Activos WHERE ACT_Codigo_Activo=%d'
sqlInsertSerie = """
    UPDATE Activos SET ACT_No_Serie=\'%s\'
    WHERE ACT_Codigo_Activo=%d"""

sqlInsertFecha = """
    UPDATE Activos SET
    ACT_Fecha_Vencimiento_Seguro=\'%s\'
    WHERE ACT_Codigo_Activo=%d"""

for r in lSeries:
    codigo = r[0][len(r[0]) - 4:len(r[0])]
    if codigo != 155:
        continue
    serie = r[1]
    garantia = r[4]
    if r[4] is None:
        garantia = 0
    cursor_new.execute(sqlGetData % int(codigo))
    fechaCompra = cursor_new.fetchone()
    if serie is not None:
        try:
            cursor_new.execute(sqlInsertSerie % (serie, int(codigo)))
        except Exception:
            print sqlInsertSerie % (serie, int(codigo))
    if fechaCompra is not None:
        if fechaCompra[0] is None:
            print 'none'
            continue
        mesesSeguro = relativedelta(months=int(garantia))
        fechaVecimiento = fechaCompra[0] + mesesSeguro
        try:
            cursor_new.execute(sqlInsertFecha % (fechaVecimiento, int(codigo)))
        except Exception:
            print sqlInsertFecha % (fechaVecimiento, int(codigo))
        # print type(fecha)
conn_new.commit()
