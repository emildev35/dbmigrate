from dbconnection import getconnection
import xlsxwriter


conn = getconnection('192.168.97.97', 'sa', 's4*Activos', 'Activos')
cursor = conn.cursor()


sql = """
	SELECT CMV_No_Documento_Referencia, ACT_Codigo_Activo, ACT_Nombre_Activo,
	DMV_Motivo_Baja, MBA_Descripcion
	FROM D_Movimientos 
	INNER JOIN C_Movimientos ON (
		CMV_No_Documento=DMV_No_Documento AND
		CMV_Dependencia=DMV_Dependencia AND
		CMV_Tipo_Movimiento=DMV_Tipo_Movimiento
	)
	INNER JOIN Activos ON (ACT_Codigo_Activo=DMV_Codigo_Activo)
	LEFT JOIN Motivos_Baja ON (MBA_Motivo_Baja=DMV_Motivo_Baja)
	WHERE CMV_Tipo_Movimiento=7 AND DMV_Motivo_Baja > 8
"""

cursor.execute(sql)

lista_erroneos = cursor.fetchall()

row = 0

file_xls = xlsxwriter.Workbook('excels/bajas_activos.xlsx')
sheet = file_xls.add_worksheet()

for error in lista_erroneos:
	for i in range(len(error)):
		sheet.write(row, i, error[i])
	row += 1


file_xls.close()
print 'Total de Activos %d' % len(lista_erroneos)