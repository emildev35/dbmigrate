from dbconnection import getconnection

con = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')
cursor = con.cursor()

try:
    cursor.execute("""exec [dbo].[Mvac_CMovimientoBaja_I] 
            @Dependencia_Id=1,@Unidad_Organizacional_Id=1,@Numero_Documento=1,
            @Fecha_Registro='2015-10-23T15:08:04',
            @Fecha_Movimiento='2015-10-23T15:08:04',
            @CI_Usuario='00000000',@No_Documento_referencia='AGIT/0037/2010',
            @Fecha_Documento_Referencia='2010-08-13T00:00:00'
            ,@Tipo_Movimiento=15,@Observaciones=''
    """)
    res = cursor.fetchall()
    print res
    con.commit()
except Exception, ex:
    print ex
