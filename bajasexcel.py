from dbconnection import getconnection


conn = getconnection('192.168.97.103', 'sa', 'ala_stg_2005', 'Activos')
cursor = conn.cursor()

conn_nuevo = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')
cursor_nuevo = conn_nuevo.cursor()

sql_resoluciones = "SELECT  DISTINCT fecha_baja, resolucion FROM TAF_BAJAS"
sql_detalles = "SELECT cod_act, fecha_baja, resolucion, motivo, observaciones FROM TAF_BAJAS WHERE resolucion='%s'"
sql_insertC = """
    INSERT INTO C_Movimientos(CMV_Dependencia, CMV_Tipo_Movimiento, CMV_No_Documento, CMV_Unidad_Organizacional_Solicitante,
    CMV_CI_Solicitante, CMV_Tipo_Documento_Referencia, CMV_No_Documento_Referencia, CMV_Fecha_Registro)
    VALUES(1, 7, %d, 1, 2381254, 7, '%s', '%s')
    """

sql_insertD = """
    INSERT INTO D_Movimientos(DMV_Dependencia, DMV_Tipo_Movimiento, DMV_No_Documento,  DMV_Codigo_Activo,
    DMV_Unidad_Organizacional, DMV_Motivo_Baja, DMV_Observacion, DMV_Fecha_Registro)
    VALUES(1, 7, %d, %d, 1, %d, '%s', '%s')
    """

cod_C = 1
cod_D = 1

cursor.execute(sql_resoluciones)
resoluciones = cursor.fetchall()


def getCodigo(oldCode):
    oldCode = str(int(oldCode))
    oldCode = oldCode[len(oldCode) - 4: len(oldCode)]
    return int(oldCode)


for resolucion in resoluciones:
    fecha = resolucion[0].strftime('%Y-%m-%d') + 'T00:00:00'
    nro_resolucion = resolucion[1]

    try:
        "Insercion del Movimiento a la Base de Datos"
        # cursor_nuevo.execute(sql_insertC % (cod_C, nro_resolucion, fecha))
        cursor.execute(sql_detalles % nro_resolucion)
        detalles = cursor.fetchall()
        for detalle in detalles:
            cod = getCodigo(detalle[0])
            fecha_detalle = detalle[1].strftime('%Y-%m-%d') + 'T00:00:00'
            id_motivo = detalle[3]
            observacion = str(detalle[4].encode('utf8', 'ignore'))
            cursor_nuevo.execute(sql_insertD % (cod_D, cod, id_motivo, observacion, fecha_detalle))
            cod_D += 1
        conn_nuevo.commit()
    except Exception, ex:
        print ex
    cod_D = 1
    cod_C += 1
