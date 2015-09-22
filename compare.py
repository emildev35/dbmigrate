from dbconnection import getconnection


conn = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')

cursor = conn.cursor()
cursor.execute('Mvac_Get_ColumnNames  Activos')

l_a = cursor.fetchall()


cursor.execute('Mvac_Get_ColumnNames  Reporte_Activos')

l_b = cursor.fetchall()

A = set(l_a)
B = set(l_b)
L = A - B

l = []
for r in L:
    l.append(r[0])

print ', '.join(l)
