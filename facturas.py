from dbconnection import getconnection


conn = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'activos')
cursor = conn.cursor(as_dict=True)

conna = getconnection('192.168.97.97', 'sa', 's4*Activos', 'Activos')
cursora = conna.cursor(as_dict=True)


sql = """SELECT * FROM TAF_FACTURA"""
sql_update = """UPDATE Activos SET ACT_No_C31='%s',
    ACT_No_Factura='%s' WHERE ACT_Codigo_Activo=%s;
    
    UPDATE Activos SET ACT_No_C31=NULL WHERE ACT_No_C31='';
    UPDATE Activos SET ACT_No_Factura=NULL WHERE ACT_No_Factura='';
    """

cursor.execute(sql)

facturas = cursor.fetchall()


def get_codigo(codigo):
    codigo = str(codigo)[len(codigo) - 4: len(codigo)]
    return str(codigo)

i = 1
for factura in facturas:
    try:
        nro_factura = factura['nro_factura']
        c_31 = factura['comprobante']
        codigo = get_codigo(factura['cod_act'])
        print "*" * 30
        print "Factura: " + nro_factura
        print "c_31 : "  +  c_31
        print "activo: "  + codigo

        cursora.execute(sql_update % (c_31, nro_factura, codigo))
        conna.commit()
        i += 1
    except Exception as e:
        conna.rollback()
        print e

print i
