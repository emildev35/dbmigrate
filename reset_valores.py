from dbconnection import getconnection


conn = getconnection('192.168.97.97', 'sa', 's4*Activos', 'Activos')
cursor = conn.cursor()


try:
    cursor.execute("""
    UPDATE Activos SET ACT_Valor_Neto=ACT_Valor_Compra, 
    ACT_Actualizacion_Acumulada_Gestion_Anterior=0,
    ACT_Depreciacion_Acumulada_Gestion_Anterior=0, 
    ACT_Actualizacion_Gestion_Actual=0,
    ACT_Depreciacion_Gestion_Actual=0, ACT_Vida_Residual=ACT_Vida_Util,
    ACT_Fecha_Ultima_Depreciacion=ACT_Fecha_Incorporacion,
    ACT_Actualizacion_Depreciacion_Acumulada=0, 
    ACT_Motivo_Baja=NULL,
    ACT_No_Informe_Baja=NULL,
    ACT_Fecha_Baja=NULL, ACT_Fecha_Ultima_Revalorizacion=NULL, 
    ACT_No_Resolucion=NULL,
    ACT_Fecha_Ultima_Mejora=NULL, ACT_Mejoras_Gestion_Actual=0,
    ACT_No_Resolucion_Baja=NULL,
    ACT_No_Informe_Mejora=NULL;
    UPDATE Activos SET ACT_Valor_Compra=5001829.58, ACT_Valor_Neto=5001829.58,
    ACT_Actualizacion_Acumulada_Gestion_Anterior=0
    WHERE ACT_Codigo_Activo=3769;
    DELETE FROM Cierre_Gestion 
    WHERE CGE_Fecha_Cierre_Gestion > '2004-01-01T00:00:00';
    UPDATE Activos SET ACT_Vida_Util=5 WHERE ACT_Grupo_Contable=5;
    """)
    conn.commit()
    print 'Operacion exitosa'
except Exception, e:
    conn.rollback()
    print e
