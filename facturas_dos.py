from dbconnection import getconnection


conn = getconnection('192.168.97.99\\DESARROLLO', 'sa', 'ADMDesarrollo2015*', 'activos')
cursor = conn.cursor(as_dict=True)

conna = getconnection('192.168.97.97', 'sa', 's4*Activos', 'Activos')
cursora = conna.cursor(as_dict=True)


sql = """SELECT ACT_No_Factura, ACT_No_C31, ACT_Codigo_Activo FROM Activos WHERE ACT_Codigo_Activo > 5085"""
sql_update = """UPDATE Activos SET ACT_No_C31='%s',
    ACT_No_Factura='%s' WHERE ACT_Codigo_Activo=%s;
    """

cursor.execute(sql)

facturas = cursor.fetchall()


def get_codigo(codigo):
    codigo = str(codigo)[len(codigo) - 4: len(codigo)]
    return str(codigo)

i = 1
for factura in facturas:
    try:
        nro_factura = factura['ACT_No_Factura']
        c_31 = factura['ACT_No_C31']
        codigo = str(factura['ACT_Codigo_Activo'])
        # print "*" * 30
        # print "Factura: " + nro_factura
        # print "c_31 : "  +  c_31
        # print "activo: "  + codigo

        cursora.execute(sql_update % (c_31, nro_factura, codigo))
        conna.commit()
        print sql_update % (c_31, nro_factura, codigo)
        i += 1
    except Exception as e:
        conna.rollback()
        print e
