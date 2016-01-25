from dbconnection import getconnection


conn = getconnection('192.168.97.97', 'sa', 's4*Activos', 'Activos')
cursor = conn.cursor()


sql_tipo = """
	SELECT GRC_Grupo_Contable, GRC_Tipo_Activo
	FROM Grupos_Contables
"""

sql_update = """
	UPDATE Activos SET ACT_Tipo_Activo = %d WHERE ACT_Grupo_Contable=%d
"""

cursor.execute(sql_tipo)
lista_tipos = cursor.fetchall()
for tipo in lista_tipos	:
	try:
		cursor.execute(sql_update % (tipo[1], int(tipo[0].strip())))
		conn.commit()
	except Exception, e:
		print e
		conn.rollback()
