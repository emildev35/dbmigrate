from dbconnection import getconnection


conn = getconnection('192.168.97.99\\ACTIVOS', 'sa', 'sa', 'Activos')
cursor = conn.cursor()

f = open('namesactivos.csv', 'r')

sql = 'UPDATE Activos set ACT_Nombre_Activo=\'%s\' WHERE ACT_Codigo_Activo=\'%s\''

count = 0
for r in f:
    r = r.replace('\n', '').split('\\')
    try:
        cursor.execute(sql % (r[1], r[0]))
        conn.commit()
    except Exception:
        count += 1


print 'Activos no modificados %d' % count
