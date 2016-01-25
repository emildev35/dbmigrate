from dbconnection import getconnection


conn = getconnection('192.168.97.97', 'sa', 's4*Activos', 'Activos')
cursor = conn.cursor()

sql = """
UPDATE D_Movimientos SET DMV_Motivo_Baja=5 WHERE DMV_Tipo_Movimiento=7 
AND DMV_Motivo_Baja=15;
UPDATE D_Movimientos SET DMV_Motivo_Baja=4 WHERE DMV_Tipo_Movimiento=7 
AND DMV_Motivo_Baja=14;
UPDATE D_Movimientos SET DMV_Motivo_Baja=6 WHERE DMV_Tipo_Movimiento=7 
AND DMV_Motivo_Baja=16;
"""

try:
	cursor.execute(sql)
	conn.commit()
except Exception, e:
	print e
	conn.rollback()